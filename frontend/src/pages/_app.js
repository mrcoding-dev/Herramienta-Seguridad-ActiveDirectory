import React from "react";
import "styles/global.scss";
import "styles/components/index.scss";
import Navbar from "components/Navbar";
import Footer from "components/Footer";

function MyApp({ Component, pageProps }) {
  return (
    <>
      <Navbar
        color="white"
        spaced={true}
        logo="https://res.cloudinary.com/dimsv0hrt/image/upload/v1670775063/so_proyecto/gs_x57glf.png"
      />

      <Component {...pageProps} />

      <Footer
        color="light"
        size="normal"
        backgroundImage=""
        backgroundImageOpacity={1}
        copyright={`© ${new Date().getFullYear()} Company`}
        logo="https://res.cloudinary.com/dimsv0hrt/image/upload/v1670775063/so_proyecto/gs_x57glf.png"
      />
    </>
  );
}

export default MyApp;
