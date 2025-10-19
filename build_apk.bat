@echo off
echo 开始构建APK...

docker run --interactive --tty --rm ^
  --volume "%cd%":/home/user/hostcwd ^
  --volume "%cd%"/.buildozer:/home/user/.buildozer ^
  buildozer/buildozer ^
  android debug

echo 构建完成！
pause