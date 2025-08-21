# Copyright (c) 2025 kick-tea All rights reserved.
import time

# 実行時間の計測開始
start_time = time.time()

sleep_time = 5  # スリープ時間を5秒に設定
print(f'Sleeping for {sleep_time} seconds...')
time.sleep(sleep_time)  # スリープ時間を待機

# 実行時間の計測終了
end_time = time.time()
execution_time = end_time - start_time

# 実行時間の表示
print('------')

print(f'Elapsed time: {execution_time:.2f}sec.')
