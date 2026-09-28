/**
 * Gestion de l'authentification JWT côté client.
 */

const TOKEN_KEY = "rf_token";
const USER_KEY = "rf_user";

// ============================================================
//  STOCKAGE DU TOKEN
// ============================================================
function saveToken(token) {
    localStorage.setItem(TOKEN_KEY, token);
}

function getToken() {
    return localStorage.getItem(TOKEN_KEY);
}

function clearToken() {
    localStorage.removeItem(TOKEN_KEY);
    localStorage.removeItem(USER_KEY);
}

function isLoggedIn() {
    return !!getToken();
}

// ============================================================
//  LOGIN / LOGOUT
// ============================================================
async function login(username, password) {
    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", password);

    const res = await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: formData,
    });

    if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.detail || "Erreur de connexion");
    }

    const data = await res.json();
    saveToken(data.access_token);
    return data;
}

function logout() {
    clearToken();
    window.location.href = "/login.html";
}

// ============================================================
//  FETCH AUTHENTIFIÉ
// ============================================================
async function authFetch(url, options = {}) {
    const token = getToken();
    if (!token) {
        window.location.href = "/login.html";
        throw new Error("Non authentifié");
    }

    const res = await fetch(url, {
        ...options,
        headers: {
            ...(options.headers || {}),
            "Authorization": `Bearer ${token}`,
        },
    });

    // Token expiré ou invalide → redirection login
    if (res.status === 401) {
        clearToken();
        window.location.href = "/login.html";
        throw new Error("Session expirée");
    }

        // 402 — Plan insuffisant
    if (res.status === 402) {
        const data = await res.json().catch(() => ({}));
        const msg = data.detail || "Cette fonctionnalité n'est pas incluse dans ton plan.";
        // Bannière discrète en haut de l'écran
        let banner = document.getElementById("upgradeBanner");
        if (!banner) {
            banner = document.createElement("div");
            banner.id = "upgradeBanner";
            banner.style.cssText = "position:fixed;top:70px;left:50%;transform:translateX(-50%);z-index:9999;background:linear-gradient(90deg,#00d4ff,#7c3aed);color:#fff;padding:14px 24px;border-radius:12px;font-weight:600;box-shadow:0 10px 30px rgba(0,0,0,.5);font-family:'Segoe UI',sans-serif;";
            document.body.appendChild(banner);
        }
        banner.textContent = "💎 " + msg + " — Passe à un plan supérieur.";
        setTimeout(() => banner.remove(), 6000);
        throw new Error("Payment Required");
    }
    return res;
}

// ============================================================
//  RÉCUPÉRATION DU PROFIL
// ============================================================
async function fetchMe() {
    const res = await authFetch("/api/auth/me");
    if (!res.ok) return null;
    return res.json();
}