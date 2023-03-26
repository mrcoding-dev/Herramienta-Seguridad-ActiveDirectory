import React from 'react'
import Head from 'next/head'

import BarraLateral from '../components/barra-lateral'
import AdminBar from '../components/admin-bar'
import LayorBar from '../components/layor-bar'

const Home = (props) => {
  return (
    <>
      <div className="home-container">
        <Head>
          <title>Fragrant Lumbering Owl</title>
          <meta property="og:title" content="Fragrant Lumbering Owl" />
        </Head>
        <BarraLateral></BarraLateral>
        <AdminBar></AdminBar>
        <LayorBar></LayorBar>
        <svg viewBox="0 0 1024 1024" className="home-icon">
          <path d="M598 298v-84h-172v84h172zM854 298q34 0 59 26t25 60v128q0 34-25 60t-59 26h-256v-86h-172v86h-256q-36 0-60-25t-24-61v-128q0-34 25-60t59-26h170v-84l86-86h170l86 86v84h172zM426 682h172v-42h298v170q0 36-25 61t-61 25h-596q-36 0-61-25t-25-61v-170h298v42z"></path>
        </svg>
      </div>
      <style jsx>
        {`
          .home-container {
            width: 100%;
            display: flex;
            overflow: auto;
            min-height: 100vh;
            align-items: flex-start;
            flex-direction: row;
            justify-content: flex-start;
          }
          .home-icon {
            width: 24px;
            height: 24px;
          }
          @media (max-width: 991px) {
            .home-icon {
              top: 31px;
              fill: #d9d9d9;
              left: 449px;
              width: 47px;
              height: 42px;
              position: absolute;
            }
          }
        `}
      </style>
    </>
  )
}

export default Home
