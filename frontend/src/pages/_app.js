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
        logo="https://static.vecteezy.com/system/resources/previews/005/499/947/original/creative-rectangle-3d-shapes-logo-modern-business-company-free-vector.jpg"
      />

      <Component {...pageProps} />

      <Footer
        color="light"
        size="normal"
        backgroundImage=""
        backgroundImageOpacity={1}
        copyright={`© ${new Date().getFullYear()} Company`}
        logo="https://static.vecteezy.com/system/resources/previews/005/499/947/original/creative-rectangle-3d-shapes-logo-modern-business-company-free-vector.jpg"
      />
    </>
  );
}

export default MyApp;
