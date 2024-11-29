import { Stack, Typography } from "@mui/material";
import { useEffect, useRef } from "react";

import { useVideoStreamContext } from "~/context/VideoSteamContext";

export const Video = () => {
  const { videoStream, removeVideoStream } = useVideoStreamContext();

  const videoRef = useRef<HTMLVideoElement | null>(null);
  const removeVideoRef = useRef<HTMLVideoElement | null>(null);

  useEffect(() => {
    if (videoRef.current !== null && videoStream !== null) {
      videoRef.current.srcObject = videoStream;
    }
  }, [videoStream]);

  useEffect(() => {
    if (removeVideoRef.current !== null && removeVideoStream !== null) {
      removeVideoRef.current.srcObject = removeVideoStream;
    }
  }, [removeVideoStream]);

  return (
    <Stack>
      <video ref={videoRef} autoPlay width="500" height="500"></video>
      <Typography>second</Typography>
      <video ref={removeVideoRef} autoPlay width="500" height="500"></video>
    </Stack>
  );
};
