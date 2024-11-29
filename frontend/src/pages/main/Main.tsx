import { Stack, Grid, Paper } from "@mui/material";

import { PlayerControls } from "~/components/playerControls/PlayerControls";
import { SideBarControls } from "~/components/sideBarControls";
import { Video } from "~/components/video/Video";

export const MainPage = () => {
  return (
    <Stack sx={{ flexGrow: 1 }}>
      <Grid container spacing={2} sx={{ flexGrow: 1, overflow: "hidden" }}>
        <Grid item xs={2}>
          <Paper sx={{ p: 2, height: "100%" }}>Side Nav</Paper>
        </Grid>
        <Grid item xs={7}>
          <Paper sx={{ p: 2, height: "100%" }}>
            <Video />
          </Paper>
        </Grid>
        <Grid item xs={3}>
          <Paper sx={{ p: 2, height: "100%" }}>
            <SideBarControls />
          </Paper>
        </Grid>
      </Grid>
      <PlayerControls />
    </Stack>
  );
};
