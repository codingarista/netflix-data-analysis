import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os


# 讓 PC & Docker 都可以找到

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data") # environment portability（環境可移植性）
OUTPUT_DIR = os.path.join(BASE_DIR, "output")


# =====================================================
# 1. Load Dataset
# =====================================================

df_movie = pd.read_csv(
    os.path.join(DATA_DIR, "netflix_movies_detailed_up_to_2025.xls")
)

df_tv = pd.read_csv(
    os.path.join(DATA_DIR, "netflix_tv_shows_detailed_up_to_2025.xls")
)


# =====================================================
# 2. Data Preprocessing
# =====================================================


# 標準化欄位名稱
df_movie.columns = df_movie.columns.str.strip().str.lower()
df_tv.columns = df_tv.columns.str.strip().str.lower()

# 加上來源標記
df_movie["content_type"] = "Movie"
df_tv["content_type"] = "TV Show"

# 合併後儲存在 df
df = pd.concat([df_movie, df_tv], ignore_index=True)

#初步檢視
print(df.head())

df = df.drop(columns=["show_id", "director", "cast", "rating", "description"])
print(df.head())


# =====================================================
# 3. Exploratory Data Analysis (EDA)
# =====================================================


print(df["content_type"].value_counts())

country_count = df['country'].value_counts().head(10)
print(country_count)

cross_tab = pd.crosstab(df['country'], df['content_type'])
print(cross_tab.sort_values(by="Movie", ascending=False).head(10))



df['country'].value_counts().head(10).plot(kind='barh', title='Top 10 Countries by Content Count')
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

print(df['release_year'].describe())

# =====================================================
# 4. Data Quality Check
# =====================================================

# 檢查每個欄位的缺失值數量與比例
missing_report = df.isnull().sum().to_frame(name="missing_count")
missing_report["missing_pct"] = (missing_report["missing_count"] / len(df)) * 100

# 顯示有缺失的欄位
missing_report = missing_report[missing_report["missing_count"] > 0]
missing_report.sort_values(by="missing_pct", ascending=False)

def check_outliers(df):
    """
    檢查 DataFrame 中所有數值欄位的異常值（IQR法），回傳統計表。
    不修改原始資料、不加欄位、不畫圖。
    """
    num_cols = df.select_dtypes(include='number').columns
    outlier_report = []

    for col in num_cols:
        series = df[col].dropna()
        if series.empty:
            continue

        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        outlier_count = ((series < lower) | (series > upper)).sum()

        outlier_report.append({
            'column': col,
            'Q1': Q1,
            'Q3': Q3,
            'IQR': IQR,
            'lower_bound': lower,
            'upper_bound': upper,
            'outlier_count': outlier_count
        })

    report_df = pd.DataFrame(outlier_report).sort_values(by='outlier_count', ascending=False)
    print("📊 數值欄位異常值報告（IQR法）：")
    return report_df
    
outliers = check_outliers(df)
print(outliers)  # 如果在 Jupyter Notebook 要改成 display(outliers)


# 檢查每個欄位的缺失值數量與比例
missing_report = df.isnull().sum().to_frame(name="missing_count")
missing_report["missing_pct"] = (missing_report["missing_count"] / len(df)) * 100

# 顯示有缺失的欄位
missing_report = missing_report[missing_report["missing_count"] > 0]
missing_report.sort_values(by="missing_pct", ascending=False)



# =====================================================
# 5. Data Cleaning
# =====================================================


df = df.copy()

# 補文字類欄位
df["genres"] = df["genres"].fillna("Unknown")
df["main_country"] = df["main_country"].fillna("Unknown")

# 補數值欄位
df["budget"] = df["budget"].fillna(0)
df["revenue"] = df["revenue"].fillna(0)

# 刪除關鍵欄位缺失資料
df = df.dropna(subset=["release_year", "duration"])

print(df.columns.tolist())

# 先標準化欄位名稱（去空白、轉小寫，避免誤判）
df_movie.columns = df_movie.columns.str.strip().str.lower()
df_tv.columns = df_tv.columns.str.strip().str.lower()

# 取出欄位集合
cols_df1 = set(df_movie.columns)
cols_df2 = set(df_tv.columns)

# 找出相同與不同的欄位
common_cols = cols_df1 & cols_df2
only_in_df1 = cols_df1 - cols_df2
only_in_df2 = cols_df2 - cols_df1

# 輸出結果
print("✅ 共同欄位：", sorted(common_cols))
print("❌ 僅 df1 有的欄位：", sorted(only_in_df1))
print("❌ 僅 df2 有的欄位：", sorted(only_in_df2))

print(df.columns)


# =====================================================
# 6. Feature Engineering
# =====================================================


country_region_map = {
    # 亞洲
    'Japan': 'Asia', 'India': 'Asia', 'South Korea': 'Asia', 'Taiwan': 'Asia', 'China': 'Asia',
    'Thailand': 'Asia', 'Philippines': 'Asia', 'Hong Kong': 'Asia',
    
    # 美洲
    'United States': 'Americas', 'Canada': 'Americas', 'Brazil': 'Americas', 'Mexico': 'Americas',
    
    # 歐洲
    'United Kingdom': 'Europe', 'France': 'Europe', 'Germany': 'Europe', 'Spain': 'Europe', 'Italy': 'Europe',
    
    # 非洲
    'Nigeria': 'Africa', 'South Africa': 'Africa',
    
    # 大洋洲
    'Australia': 'Oceania', 'New Zealand': 'Oceania'
}

# main country

df["main_country"] = (
    df["country"]
    .str.split(",")
    .str[0]
    .str.strip()
)

df["main_country"] = df["main_country"].fillna("Unknown")


# region

df["region"] = (
    df["main_country"]
    .map(country_region_map)
    .fillna("Other")
)

# 建立 release_decade（年代分群)
df['release_decade'] = (df['release_year'] // 10 * 10).astype(str) + 's'

# === 建立 ROI（投資報酬率
df['ROI'] = np.where(
    df['budget'] > 0,
    (df['revenue'] - df['budget']) / df['budget'],
    np.nan
)

# === Step 5：建立 vote_group（評分分群）===
def classify_vote(score):
    if score >= 8:
        return "High"
    elif score >= 6:
        return "Medium"
    else:
        return "Low"

df['vote_group'] = df['vote_average'].apply(classify_vote)


# 提取數字與單位
def parse_duration(x):
    try:
        n, unit = x.strip().split(maxsplit=1)
        return int(n), unit.strip()
    except:
        return pd.NA, pd.NA

# 應用後解包
duration_parsed = df['duration'].apply(parse_duration)
df['duration_int'] = duration_parsed.apply(lambda x: x[0])
df['duration_unit'] = duration_parsed.apply(lambda x: x[1])

print(df[['duration', 'duration_int', 'duration_unit']].dropna().head(10))


# =====================================================
# 7. Export Clean Dataset
# =====================================================


df.to_csv(
    os.path.join(OUTPUT_DIR, "netflix_c_2025.csv"),
    index=False
)

print("✅ Analysis completed successfully")

