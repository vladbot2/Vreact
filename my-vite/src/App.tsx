import { GoogleLogin } from '@react-oauth/google'
import axios from 'axios'

function App() {

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
        }
    }

    return (
        <div style={{ padding: 40 }}>
            <h2>Google Login</h2>

            <GoogleLogin
                onSuccess={loginGoogle}
                onError={() => console.log('error')}
            />
        </div>
    )
}

export default App
