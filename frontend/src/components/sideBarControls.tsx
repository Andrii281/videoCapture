import { Button, Stack } from "@mui/material";

import { videoStreamApi } from "~/streamApi/videoStream";

export const SideBarControls = () => {
  const handleSendMessage = () => {
    videoStreamApi.sendMessage();
  };

  const makeCall = () => {
    videoStreamApi.makeCall();
  };

  return (
    <Stack>
      <Button onClick={handleSendMessage}>Test request</Button>
      <Button onClick={makeCall}>offer</Button>
    </Stack>
  );
};
