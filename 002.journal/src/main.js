import App from './App.svelte';
import "./global.css";
import { HandleSession } from './lib/Session';
import { profile, token } from './stores';

const app = (async () => {
    const [profileData, tokenData] = await HandleSession(0);
    profile.set(profileData || null);
    token.set(tokenData || null);
    return new App({
        target: document.body,
        props: {
            name: "Svelte"
        }
    })
})()

export default app;