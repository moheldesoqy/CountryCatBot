{ pkgs }: {
  deps = [
    pkgs.ffmpeg_6-full.bin
    pkgs.libopus
    pkgs.wget
  ];
}