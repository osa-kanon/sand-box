# Copyright (c) 2025 kick-tea All rights reserved.
import time

# 実行時間の計測開始
start_time = time.time()

print('------')

def _upload_intern(self, messages: list):
    for m in messages:
        json_str = json.dumps(m)
        cmd = ["scribe_cat", self.category, json_str]
        subprocess.run(cmd)
      
print(f'Elapsed time: {execution_time:.2f}sec.')
