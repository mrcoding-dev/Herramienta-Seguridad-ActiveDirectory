import React from "react";
import Meta from "components/Meta";
import SearchSection from "components/SearchSection";

function IndexPage(props) {
  return (
    <>
      <Meta />
      <SearchSection
        color="white"
        size="medium"
        backgroundImage=""
        backgroundImageOpacity={1}
        title="Buscador de Cuentas en Desuso"
        buttonColor="primary"
        buttonInverted={false}
        buttonPath="/"
      />
    </>
  );
}

export default IndexPage;
