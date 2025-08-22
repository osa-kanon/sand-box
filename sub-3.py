# Copyright (c) 2025 kick-tea All rights reserved.
import time

# 実行時間の計測開始
start_time = time.time()

sleep_time = 5  # スリープ時間を5秒に設定
print(f'Sleeping for {sleep_time} seconds...')
time.sleep(sleep_time)  # スリープ時間を待機

## add start
set -e # exit on error

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <lexicon> <dict_dir>"
  exit 1
fi

lexicon=$1
dir=$2

mkdir -p $dir

cat $lexicon |
  awk '{ for(n=2;n<=NF;n++){ phones[$n] = 1; }} END{for (p in phones) print p;}' |
  grep -v sp >$dir/nonsilence_phones.txt || exit 1

(
  echo sp
  echo spn
) >$dir/silence_phones.txt

echo sp >$dir/optional_silence.txt
## add end

# 実行時間の計測終了
end_time = time.time()
execution_time = end_time - start_time

# 実行時間の表示
print('------')
print(f'Elapsed time: {execution_time:.2f}sec.')