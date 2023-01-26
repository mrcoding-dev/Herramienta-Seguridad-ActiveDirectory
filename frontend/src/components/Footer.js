import React from "react";
import Link from "next/link";
import Section from "components/Section";

function Footer(props) {
  return (
    <Section
      color={props.color}
      size={props.size}
      backgroundImage={props.backgroundImage}
      backgroundImageOpacity={props.backgroundImageOpacity}
      className="footer"
    >
      <div className="FooterComponent__container container">
        <div className="brand left">
          <Link href="/">
            <a>
              <img src={props.logo} alt="Logo" />
            </a>
          </Link>
        </div>
        <div className="links right">
          <Link href="/">
            <a>Sobre</a>
          </Link>
          <Link href="/">
            <a></a>
          </Link>
          <Link href="/">
            <a>Contacto</a>
          </Link>
          <a
            target="_blank"
            href="#"
            rel="noopener noreferrer"
          >

          </a>
        </div>
        <div className="social right">
          <a
            href="#"
            target="_blank"
            rel="noopener noreferrer"
          >
            <span className="icon">
              <i className="fab fa-twitter" />
            </span>
          </a>
          <a
            href="#"
            target="_blank"
            rel="noopener noreferrer"
          >
            <span className="icon">
              <i className="fab fa-facebook-f" />
            </span>
          </a>
          <a
            href="#"
            target="_blank"
            rel="noopener noreferrer"
          >
            <span className="icon">
              <i className="fab fa-instagram" />
            </span>
          </a>
        </div>
        <div className="copyright left">
          {props.copyright}
          <Link href="#">
            <a></a>
          </Link>
          <Link href="#">
            <a></a>
          </Link>
        </div>
      </div>
    </Section>
  );
}

export default Footer;
