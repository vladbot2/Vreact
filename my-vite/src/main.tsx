<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 456b6310aad55a6943e785cf21b6c6f5a78ee605
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import { GoogleOAuthProvider } from '@react-oauth/google'

ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
<<<<<<< HEAD
        <GoogleOAuthProvider clientId="ТВІЙ_GOOGLE_CLIENT_ID">
            <App />
        </GoogleOAuthProvider>
    </React.StrictMode>
=======
        <GoogleOAuthProvider clientId="ТУТ_ТВІЙ_GOOGLE_CLIENT_ID">
            <App />
        </GoogleOAuthProvider>
    </React.StrictMode>
=======
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import {BrowserRouter} from "react-router-dom";
import ScrollToTop from "./functional/ScrollToTop.tsx";
import {GoogleOAuthProvider} from "@react-oauth/google";

createRoot(document.getElementById('root')!).render(
  <StrictMode>
      <BrowserRouter>
          <GoogleOAuthProvider clientId={"688315354046-isd3q5qkjaj88uaj9oudrldsf18bm592.apps.googleusercontent.com"}>
             <ScrollToTop>
                 <App />
             </ScrollToTop>
          </GoogleOAuthProvider>
      </BrowserRouter>
  </StrictMode>,
>>>>>>> 0836948cd765c84e457c61238868684ca2780c47
>>>>>>> 456b6310aad55a6943e785cf21b6c6f5a78ee605
)
