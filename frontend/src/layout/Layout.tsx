import { Stack } from "@mui/material";

import { Header } from "~/components/header/Header";
import { MainPage } from "~/pages/main/Main";

export const Layout = () => {
  return (
    <Stack sx={{ width: "100%", minHeight: "100vh" }}>
      <Header />
      <MainPage />
    </Stack>
  );
};
