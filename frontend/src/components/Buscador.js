import React, { useEffect, useState } from "react";
import algoliasearch from "algoliasearch/lite";
import {Hits, InstantSearch, SearchBox, Highlight, RefinementList,Pagination,Configure } from "react-instantsearch-hooks-web";
import 'instantsearch.css/themes/satellite.css';
//const searchClient = algoliasearch(`${process.env.APP_ID}`,`${process.env.API_KEY}`);
const searchClient = algoliasearch('9W91AT7FGX','057820d6843d2ec7e052917d89739468');


function Hit({ hit }) {
    return (
        <article className="hit-container">
            <h1 className="hit-title">
                <Highlight attribute="nombres" hit={hit} />
            </h1>
            <div className="hit-details">
                <div className="hit-rut">
                    <strong>Rut:</strong>{" "}
                    <Highlight attribute="rut" hit={hit} />
                </div>
                <div className="hit-usernt">
                    <strong>Username:</strong>{" "}
                    <Highlight attribute="usernt" hit={hit} />
                </div>
                <div className="hit-empresa">
                    <strong>Empresa:</strong>{" "}
                    <Highlight attribute="empresa" hit={hit} />
                </div>
            </div>
        </article>
    );
}


function Buscador() {
    const [showHits, setShowHits] = useState(false);
    const [query, setQuery] = useState('');
    return (
        <div className="container" >

            <InstantSearch searchClient={searchClient} indexName="dev_security" >
                <Configure hitsPerPage={1} />
                <SearchBox onFocus={()=>setShowHits(true)} onBlur={()=>setShowHits(false)}/>
                <RefinementList attribute="empresa"/>
                {showHits ? <Hits hitComponent={Hit} /> : null}

            </InstantSearch>
        </div>
    );
}
export default Buscador;