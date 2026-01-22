<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 456b6310aad55a6943e785cf21b6c6f5a78ee605
import { GoogleLogin } from '@react-oauth/google'
import axios from 'axios'

function App() {

<<<<<<< HEAD
    const loginGoogle = async (cred: any) => {
        try {
            const res = await axios.post(
                'http://127.0.0.1:8000/api/users/google/',
                {
                    token: cred.credential,
                }
            )

            console.log('login ok', res.data)
            localStorage.setItem('token', res.data.token)

        } catch (e) {
            console.log('login error', e)
=======
    const handleLogin = async (credentialResponse: any) => {
        try {
            const res = await axios.post(
                'http://127.0.0.1:8000/api/auth/google/',
                {
                    access_token: credentialResponse.credential,
                }
            )

            console.log('login success', res.data)
        } catch (error) {
            console.log('login error', error)
>>>>>>> 456b6310aad55a6943e785cf21b6c6f5a78ee605
        }
    }

    return (
        <div style={{ padding: 40 }}>
            <h2>Google Login</h2>

            <GoogleLogin
<<<<<<< HEAD
                onSuccess={loginGoogle}
=======
                onSuccess={handleLogin}
>>>>>>> 456b6310aad55a6943e785cf21b6c6f5a78ee605
                onError={() => console.log('error')}
            />
        </div>
    )
}

export default App
<<<<<<< HEAD
=======
=======
import Register from "./Register";

function App() {
    return <Register />;
}

export default App;
>>>>>>> 0836948cd765c84e457c61238868684ca2780c47
>>>>>>> 456b6310aad55a6943e785cf21b6c6f5a78ee605
