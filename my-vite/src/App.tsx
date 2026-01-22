<<<<<<< HEAD
import { GoogleLogin } from '@react-oauth/google'
import axios from 'axios'

function App() {

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
        }
    }

    return (
        <div style={{ padding: 40 }}>
            <h2>Google Login</h2>

            <GoogleLogin
                onSuccess={handleLogin}
                onError={() => console.log('error')}
            />
        </div>
    )
}

export default App
=======
import Register from "./Register";

function App() {
    return <Register />;
}

export default App;
>>>>>>> 0836948cd765c84e457c61238868684ca2780c47
