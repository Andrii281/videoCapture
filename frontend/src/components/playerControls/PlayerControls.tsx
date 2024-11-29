import { Stack, Button } from "@mui/material";

import { useVideoStreamContext } from "~/context/VideoSteamContext";
import { videoStreamApi } from "~/streamApi/videoStream";

export const PlayerControls = () => {
  const { startRecording, stopRecording, isRecording } = useVideoStreamContext();
  const handleOnRecord = async () => {
    if (isRecording) {
      stopRecording();
    } else {
      await videoStreamApi.makeCall();
      startRecording();
    }
  };

  return (
    <Stack sx={{ width: "100%", height: "3rem", background: "red" }} alignItems="center" justifyContent="center">
      <Button onClick={handleOnRecord}>Record</Button>
    </Stack>
  );
};
