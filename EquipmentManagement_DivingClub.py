#出力結果は空白
import pandas as pd
import os

def clean_numeric_data(df, columns):
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def filter_data(new_student_height, new_student_weight, new_student_boot):
    # 現在のディレクトリにあるエクセルファイルを読み込む
    input_file = "U.R.D.C. 器材管理2024 調整版.xlsx"
    if not os.path.exists(input_file):
        print(f"エラー: {input_file} が見つかりません。")
        return

    # Excelファイルを読み込む
    df = pd.read_excel(input_file)

    # 列名を表示して確認
    print("ファイルに含まれる列名:")
    print(df.columns)

    # 数値データのクリーニング
    numeric_columns = ['身長', '体重', 'ブーツ']
    df = clean_numeric_data(df, numeric_columns)

    # 無効なデータを含む行を削除
    df = df.dropna(subset=numeric_columns)

    # データをフィルタリング
    filtered_df = df[
        (df['身長'].between(new_student_height - 5, new_student_height + 5)) &
        (df['体重'].between(new_student_weight - 10, new_student_weight + 10)) &
        (df['ブーツ'].between(new_student_boot - 3, new_student_boot + 3))
    ]

    # 表示する列を選択
    columns_to_display = ['名前', '身長', '体重', 'ブーツ', 'オプチ', '適正(ジャケ有)', '適正(ジャケ無)', '期']

    # 結果を表示
    print("\nマッチング結果:")
    print(f"条件に一致するデータ数: {len(filtered_df)}")
    print("\n以下のデータが新入生の条件に近いです:")

    if len(filtered_df) > 0:
        # 必要な列のみを表示
        filtered_df = filtered_df[columns_to_display]

        # データフレームを文字列として整形
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_rows', None)
        print(filtered_df.to_string(index=False))
    else:
        print("条件に一致するデータはありませんでした。")

    # 無効なデータの報告
    invalid_data = df[df[numeric_columns].isna().any(axis=1)]
    if not invalid_data.empty:
        print("\n警告: 以下の行には無効なデータが含まれていたため、フィルタリングから除外されました:")
        print(invalid_data.to_string(index=True))

# メイン実行部分
if __name__ == "__main__":
    try:
        new_student_height = float(input("新入生の身長を入力してください (cm): "))
        new_student_weight = float(input("新入生の体重を入力してください (kg): "))
        new_student_boot = float(input("新入生のブーツサイズを入力してください (cm): "))

        filter_data(new_student_height, new_student_weight, new_student_boot)
    except ValueError:
        print("エラー: 正しい数値を入力してください。")
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")
        


#パイプで出力させる
# import pandas as pd
# import os

# def clean_numeric_data(df, columns):
#     for col in columns:
#         df[col] = pd.to_numeric(df[col], errors='coerce')
#     return df

# def filter_data(new_student_height, new_student_weight, new_student_boot):
#     # 現在のディレクトリにあるエクセルファイルを読み込む
#     input_file = "U.R.D.C. 器材管理2024 調整版.xlsx"
#     if not os.path.exists(input_file):
#         print(f"エラー: {input_file} が見つかりません。")
#         return

#     # Excelファイルを読み込む
#     df = pd.read_excel(input_file)

#     # 列名を表示して確認
#     print("ファイルに含まれる列名:")
#     print(df.columns)

#     # 数値データのクリーニング
#     numeric_columns = ['身長', '体重', 'ブーツ']
#     df = clean_numeric_data(df, numeric_columns)

#     # 無効なデータを含む行を削除
#     df = df.dropna(subset=numeric_columns)

#     # データをフィルタリング
#     filtered_df = df[
#         (df['身長'].between(new_student_height - 5, new_student_height + 5)) &
#         (df['体重'].between(new_student_weight - 10, new_student_weight + 10)) &
#         (df['ブーツ'].between(new_student_boot - 3, new_student_boot + 3))
#     ]

#     # 表示する列を選択
#     columns_to_display = ['名前', '身長', '体重', 'ブーツ', 'オプチ', '適正(ジャケ有)', '適正(ジャケ無)', '期']

#     # 結果を表示
#     print("\nマッチング結果:")
#     print(f"条件に一致するデータ数: {len(filtered_df)}")
#     print("\n以下のデータが新入生の条件に近いです:")

#     if len(filtered_df) > 0:
#         # 必要な列のみを表示
#         filtered_df = filtered_df[columns_to_display]

#         # データフレームをパイプで区切って表示
#         pd.set_option('display.max_columns', None)
#         pd.set_option('display.width', None)
#         pd.set_option('display.max_rows', None)
#         print(filtered_df.to_csv(sep='|', index=False))
#     else:
#         print("条件に一致するデータはありませんでした。")

#     # 無効なデータの報告
#     invalid_data = df[df[numeric_columns].isna().any(axis=1)]
#     if not invalid_data.empty:
#         print("\n警告: 以下の行には無効なデータが含まれていたため、フィルタリングから除外されました:")
#         print(invalid_data.to_csv(sep='|', index=True))

# # メイン実行部分
# if __name__ == "__main__":
#     try:
#         new_student_height = float(input("新入生の身長を入力してください (cm): "))
#         new_student_weight = float(input("新入生の体重を入力してください (kg): "))
#         new_student_boot = float(input("新入生のブーツサイズを入力してください (cm): "))

#         filter_data(new_student_height, new_student_weight, new_student_boot)
#     except ValueError:
#         print("エラー: 正しい数値を入力してください。")
#     except Exception as e:
#         print(f"エラーが発生しました: {str(e)}")


#出力結果の例
'''
(base) yamawakidaiki@DMacBook-Air urdc器材管理 % python 器材管理.py
新入生の身長を入力してください (cm): 171
新入生の体重を入力してください (kg): 73
新入生のブーツサイズを入力してください (cm): 26.5
ファイルに含まれる列名:
Index(['名前', '身長', '体重', 'ブーツ', 'オプチ', '適正(ジャケ有)', '適正(ジャケ無)', '期', '学部/コース',
    '性', 'Unnamed: 10', 'マスク', 'シュノーケル', 'ロングジョン', 'ジャケット', 'ナイフ', 'ブーツ.1',
    'グローブ'],
    dtype='object')

マッチング結果:
条件に一致するデータ数: 4

以下のデータが新入生の条件に近いです:
	名前    身長   体重  ブーツ        オプチ 適正(ジャケ有)  適正(ジャケ無)    期
	name 1 173.0 71.0 26.5        度無し        5       3.0 51.0
	name 2 166.0 64.0 26.5        度無し      NaN       NaN 53.0
	name 3 176.0 68.0 28.5 左-6.0右-5.5      NaN       NaN 54.0
	name 4 174.0 72.5 27.0     両方-4.0      NaN       NaN 54.0
'''
