# 📌 RÉSUMÉ DE PASSATION – Portfolio, Blog RF & SaaS Dashboard

**Dernière mise à jour** : 25 septembre 2026
**Propriétaire** : Jean Thomas Montezuma Montreuil
**Email** : jeant.montreuil@gmail.com
**Téléphone** : +1 438 860 6766
**LinkedIn** : https://www.linkedin.com/in/jean-thomas-montezuma-montreuil-383aa813/

---

## 1. Contexte

Écosystème technique complet pour un ingénieur RF Senior (15+ ans d'expérience) :
- Portfolio professionnel en ligne
- Veille d'offres d'emploi automatisée
- Blog technique automatisé avec sources citées
- Dashboard OpenRAN (futur SaaS)
- Générateur de candidatures assisté par IA

**Stack** : Python, HTML/CSS/JS, FastAPI, GitHub Actions, Render, Groq API, Adzuna API, Resend, Docker, PostgreSQL (à venir), Stripe (à venir).
---

## 2. Dépôts et URLs

| Ressource | URL |
|---|---|
| GitHub | https://github.com/mmjt2000/portfolio |
| Site principal | https://mon-site-rf.onrender.com |
| Blog | https://mon-site-rf.onrender.com/blog.html |
| À propos du blog | https://mon-site-rf.onrender.com/blog/about.html |
| Flux RSS (validé W3C) | https://mon-site-rf.onrender.com/blog/feed.xml |
| Dashboard OpenRAN | https://rf-engineering-2-0.onrender.com |
| Repo Dashboard | https://github.com/mmjt2000/rf-engineering-2-0 |
| Render Dashboard | https://dashboard.render.com |

---

## 3. Fichiers clés (dossier Mon site/)

| Fichier | Rôle |
|---|---|
| index.html | Portfolio principal |
| jobs.html | Liste des offres d'emploi RF |
| jobs.json | Données des offres |
| blog.html | Listing des articles |
| blog/about.html | Page À propos + politique de citation |
| blog/feed.xml | Flux RSS généré |
| blog/article-*.html | Articles générés |
| bibliography.bib | Base BibTeX des sources |
| generate_blog.py | Génère les articles |
| prepare_application.py | CV + lettre + prépa auto |
| prepare_manual.py | Mode manuel |
| manual_offer.txt | Offre manuelle à remplir |
| fetch_jobs.py | Récupère les offres Adzuna |
| send_jobs_email.py | Email récap via Resend |
| update_news.py | Met à jour la section News |
| clean_orphan_articles.py | Supprime les articles orphelins |
| add_copyright.py | En-tête copyright .py |
| add_copyright_html.py | En-tête copyright .html |
| LICENSE | All Rights Reserved |
| images/photo.jpg | Photo de profil |
| .github/workflows/ | Automatisations GitHub Actions |

---

## 4. Variables d'environnement & Secrets

### En local (PowerShell)
GROQ_API_KEY
ADZUNA_APP_ID
ADZUNA_APP_KEY
RESEND_API_KEY
EMAIL_TO

### GitHub Secrets
GROQ_API_KEY, ADZUNA_APP_ID, ADZUNA_APP_KEY, RESEND_API_KEY, EMAIL_TO

### Render Environment
GROQ_API_KEY

ATTENTION : Ne jamais committer ces clés.

---

## 5. État actuel du projet (Septembre 2026)

### Ce qui est terminé

| Composant | Statut |
|---|---|
| Portfolio | En ligne avec photo + téléphone |
| Veille d'offres | Automatisée via Adzuna |
| Blog technique | 6 articles, design pro |
| Idée 1 : Automatisation blog | Workflow GitHub Actions |
| Idée 2 : Page À propos | Créée et liée |
| Idée 3 : Temps de lecture + LinkedIn | Sur chaque article |
| Idée 4 : Flux RSS | Validé W3C |
| Idée 5 : 7 sources RSS | Ericsson, Nokia, Huawei, O-RAN, 3GPP, IEEE, Light Reading |
| Protection juridique | LICENSE + 31 en-têtes copyright |
| Dashboard OpenRAN | Déployé en Docker sur Render |
| Préparation candidatures | Manuelle + automatique |

### Blog actuel
- 6 articles générés automatiquement
- Anti-doublon actif (ID stable sur URL source)
- 2 articles max par exécution, chaque lundi 8h Montréal
- Sources citées avec clés BibTeX

---

## 6. Points de vigilance

- Toujours faire git pull avant de modifier blog.html ou index.html
- Ne pas modifier blog.html si GitHub Actions vient de tourner
- Vérifier bibliography.bib (6+ entrées)
- Badge RSS W3C : pas de hotlink (texte cliquable)
- update_news.py réécrit index.html : vérifier l'en-tête copyright

---

## 7. Comment reprendre le travail

### Installation
git clone https://github.com/mmjt2000/portfolio.git
cd portfolio
pip install feedparser

### Configuration
Définir les variables d'environnement (voir section 4)

### Scripts principaux
python generate_blog.py
python fetch_jobs.py
python send_jobs_email.py
python prepare_manual.py
python clean_orphan_articles.py
python add_copyright.py
python add_copyright_html.py

### Publier
git add .
git commit -m "..."
git pull
git push

---

## 8. Plan SaaS – Monétisation du Dashboard OpenRAN

### 8.1 Vision
Transformer rf-engineering-2-0 en SaaS multi-tenant monétisable.

### 8.2 Architecture cible
Frontend → FastAPI (JWT + Tenant Middleware + Stripe)
             → PostgreSQL (multi-tenant + billing)
             → Redis (cache + sessions)

### 8.3 Stack technique (MISE À JOUR - Oracle Cloud)

- **Hébergement principal** : Oracle Cloud Always Free (VM ARM 4 CPU / 24 GB)
- **Région** : Canada Southeast (Montréal) - parfait pour le Québec
- **Tenancy Oracle** : jeantmontreuil
- **Backend** : FastAPI + SQLAlchemy + Alembic (Docker)
- **Base de données** : PostgreSQL 16 (self-hosted sur Oracle)
- **Cache/Sessions** : Redis 7 (self-hosted sur Oracle)
- **Reverse proxy** : Nginx + Let's Encrypt
- **Auth** : JWT + python-jose + passlib
- **Paiement** : Stripe Billing
- **Emails** : Resend (ou Oracle Email Delivery)
- **CI/CD** : GitHub Actions → Docker Registry → Oracle VM
- **Backup** : Oracle boot volume snapshots automatiques

**Compte Oracle Cloud** : actif depuis septembre 2026
**VCN existant** : vcn-20260920-2316
**VM à créer** : rf-saas-prod (ARM Ampere A1)

### 8.4 Plan d'action en 6 phases

| Phase | Description | Durée |
|---|---|---|
| Phase 1 | Restructuration du code | 1-2 sem |
| Phase 2 | Multi-tenancy des données | 2 sem |
| Phase 3 | Authentification | 1-2 sem |
| Phase 4 | Onboarding & plans | 1 sem |
| Phase 5 | Intégration Stripe | 2-3 sem |
| Phase 6 | Opérations | continu |

Total Phase 1-5 : ~10 semaines à temps partiel (5-10h/semaine).

### 8.5 Modèle économique
SaaS par site avec 4 niveaux :

| Plan | Prix/mois | Sites max | Users max |
|---|---|---|---|
| Trial | 0$ (14j) | 3 | 2 |
| Starter | 490$ | 10 | 5 |
| Pro | 1490$ | 50 | 20 |
| Enterprise | Sur devis | Illimité | Illimité |

### 8.6 Points critiques
- Fuite de données : tests isolation
- Webhook Stripe : idempotence + retry
- Coût infra : Render free tier
- RGPD : politique + droit effacement
- Sécurité JWT : rotation + 24h

### 8.7 Première action
Phase 1, étape 1.1 : créer app/, frontend/, tests/

### 8.8 Travaux à faire - Prochaine session

**PRIORITÉ 1 : Setup Oracle Cloud**

État actuel :
- [x] Compte Oracle Cloud créé
- [x] VCN configuré (vcn-20260920-2316)
- [ ] VM ARM Ampere A1 à créer
- [ ] Docker + Docker Compose à installer
- [ ] Nginx + Let's Encrypt à configurer
- [ ] PostgreSQL + Redis à déployer
- [ ] FastAPI à déployer
- [ ] CI/CD GitHub Actions à mettre en place

**Prochaine action immédiate :**
Créer la VM ARM Ampere A1 dans Oracle Cloud :
- Menu → Compute → Instances → Create Instance
- Name : rf-saas-prod
- Image : Ubuntu 22.04
- Shape : VM.Standard.A1.Flex (4 OCPU, 24 GB)
- Public IP : activée
- SSH keys : générer et sauvegarder la clé privée

**Ensuite (dans l'ordre) :**
1. Se connecter en SSH à la VM
2. Installer Docker + Docker Compose
3. Créer le docker-compose.yml (PostgreSQL + Redis + FastAPI + Nginx)
4. Configurer un domaine + SSL Let's Encrypt
5. Mettre en place le pipeline CI/CD GitHub Actions → Oracle VM
6. Commencer la Phase 1 du SaaS (restructuration du code)

---

## 9. Sécurité – Actions urgentes

### Clé Groq à révoquer
La clé API Groq actuelle a été exposée dans des captures.

Action immédiate :
1. Aller sur https://console.groq.com
2. Supprimer la clé compromise
3. Créer une nouvelle clé
4. Stocker dans variables d'env et secrets GitHub

### Protection du code
- LICENSE All Rights Reserved
- 31 fichiers avec en-tête copyright
- .gitignore configuré
- Recommandé : activer GitHub Secret Scanning

### Vérification historique
git log -p --all | Select-String -Pattern "gsk_"

---

## 10. Idées bonus (backlog)

| Idée | Effort | Impact |
|---|---|---|
| Articles manuels (Markdown) | Moyen | Élevé |
| Moteur de recherche blog | Moyen | Élevé |
| Catégories d'articles | Moyen | Moyen |
| Page Contact formulaire | Rapide | Moyen |
| Analytics (Plausible) | Rapide | Moyen |
| Page Consulting | Moyen | Élevé |
| Media kit Sponsors | Moyen | Moyen |
| Formation en ligne | Élevé | Élevé |
| Setup Oracle Cloud SaaS | Élevé | Critique |

---

## 11. Pour un nouvel assistant

1. Les 5 idées du blog sont terminées
2. Le blog est autonome (GitHub Actions chaque lundi)
3. Protection en place : LICENSE + 31 en-têtes
4. URGENT : révoquer la clé Groq exposée
5. Prochain chantier : SaaS multi-tenant (Phase 1-5)
6. Approche : pas à pas, tester à chaque étape
7. Compte Oracle Cloud actif (tenancy jeantmontreuil, région Montréal)
8. Prochaine session : créer VM ARM Ampere A1 pour héberger le SaaS

---

## 12. Style de travail

Ce projet a été construit pas à pas :
- Une idée à la fois
- Test à chaque étape
- Correction immédiate
- Documentation continue

---


## 13. Mise à jour du 26 septembre 2026 — RESTRUCTURATION COMPLÈTE

### Statut : PHASE 1 TERMINÉE ✅

### Fichiers restructurés

Le monolithe `backend/main.py` (370 lignes) a été découpé en modules :
rf-engineering-2-0/
├── backend/
│ ├── main.py ← Point d'entrée minimal (import app.main)
│ ├── requirements.txt
│ └── app/
│ ├── init.py
│ ├── main.py ← App FastAPI + routers + WebSocket
│ ├── config.py ← Constantes (clusters, technos, paramètres)
│ ├── background.py ← Boucle temps réel (broadcast KPI/SON)
│ ├── data/
│ │ ├── cells.py ← gen_cells(), CELLS, CELLS_BY_ID
│ │ ├── kpi.py ← gen_kpi(), compute_health()
│ │ ├── outages.py ← Gestion des pannes
│ │ ├── heatmap.py ← RSRP interpolation IDW
│ │ └── drivetest.py ← Parcours drive test simulé
│ ├── son/
│ │ └── engine.py ← Templates SON + buffer d'événements
│ ├── websocket/
│ │ └── manager.py ← ConnectionManager
│ └── routers/
│ ├── cells.py ← /api/cells, /api/kpi/*, /api/heatmap...
│ ├── son.py ← /api/son/events
│ └── export.py ← /api/export/csv
└── frontend/
└── index.html

text

### Résultat

- ✅ API REST fonctionnelle : 54 cellules, KPIs, heatmap, drive test
- ✅ WebSocket temps réel (broadcast toutes les 2s)
- ✅ SON Engine actif (MRO, MLB, CCO, ANR, ICIC, Self-Healing, PCI)
- ✅ Export CSV opérationnel
- ✅ Déployé sur Render : https://rf-engineering-2-0.onrender.com
- ✅ Testé en local (uvicorn) + en ligne

### Notes importantes

1. **⚠️ OneDrive problème** : le projet a été déplacé vers `C:\Dev\rf-engineering-2-0\`
   pour éviter les conflits de fichiers virtuels. **Travailler depuis `C:\Dev\`,
   plus jamais depuis OneDrive.**

2. **⚠️ BOM UTF-8** : lors de la création de fichiers Python avec PowerShell,
   le BOM UTF-8 a corrompu plusieurs fichiers. Utiliser **Notepad** ou **VS Code**
   avec encodage **UTF-8 sans BOM**.

3. **Dépôt GitHub** : https://github.com/mmjt2000/rf-engineering-2-0
   (Push forcé car l'ancien commit était plus ancien)

4. **Render** : redéploiement automatique activé sur chaque push.

### Prochaines étapes — PHASE 2

- [ ] Créer `app/models/` (SQLAlchemy) : tenant, user, site, cell
- [ ] Créer `app/schemas/` (Pydantic) : validation des données
- [ ] Créer `app/services/` : logique métier
- [ ] Base de données PostgreSQL (Railway ou Render)
- [ ] Authentification JWT + multi-tenant
- [ ] Règles d'isolation par tenant
- [ ] Tests unitaires + tests d'isolation

---

## 14. Mise à jour du 27 septembre 2026 — PHASE 2 : MULTI-TENANCY & AUTH

### Statut : PHASE 2 TERMINÉE ✅

### Base de données PostgreSQL (Neon.tech)

- **Provider** : Neon.tech (gratuit à vie, 0,5 GB)
- **Région** : AWS US East 2 (Ohio)
- **Projet Neon** : `rf-engineering`
- **URL connexion** : `postgresql+psycopg://neondb_owner:***@ep-lingering-fog-...neon.tech/neondb?sslmode=require`
- **⚠️ Variable `DATABASE_URL`** stockée dans `backend/.env` (jamais commité)

### Modèles SQLAlchemy créés

| Modèle | Fichier | Champs clés |
|---|---|---|
| **Tenant** | `app/models/tenant.py` | id, name, slug, plan, stripe_customer_id, is_active |
| **User** | `app/models/user.py` | id, tenant_id, email, hashed_password, role, is_active, last_login |
| **Site** | `app/models/site.py` | id, tenant_id, name, lat, lon, cluster |
| **Cell** | `app/models/cell.py` | id, site_id, cell_id, techno, pci, azimuth, tilt_e, tilt_m, tx_power, height_m, band |

**Tables créées dans Neon** : `tenants`, `users`, `sites`, `cells` ✅

### Authentification JWT

**Fichiers créés :**
- `app/database.py` — engine + session + `get_db()`
- `app/dependencies.py` — `get_current_user()`, `get_current_tenant_id()`, `get_current_tenant()`, `require_feature()`
- `app/services/auth_service.py` — hash, verify, create_token, decode
- `app/services/tenant_service.py` — CRUD tenant
- `app/schemas/user.py` — Pydantic UserCreate, UserLogin, UserRead, Token
- `app/schemas/tenant.py` — Pydantic TenantCreate, TenantRead
- `app/routers/auth.py` — signup, login, me

**Configuration dans `app/config.py` :**
```python
SECRET_KEY = os.environ.get("SECRET_KEY", "...")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24h
Variable SECRET_KEY ajoutée dans .env.

Gating par plan (require_feature)
Plans définis dans app/dependencies.py :

Plan	Sites max	Users max	Features
trial	3	2	kpis_basic, map
starter	10	5	+ son, export_csv
pro	50	20	+ heatmap, self_healing
enterprise	illimité	illimité	all
Utilisation dans les routes :

python
@router.get("/api/son/events")
def son_events(
    tenant_id: int = Depends(get_current_tenant_id),
    _ = Depends(require_feature("son")),
):
    ...
Routes protégées (Phase 2)
Toutes les routes RF nécessitent maintenant :

Un JWT valide (sinon 401 Unauthorized)

Le plan adéquat (sinon 402 Payment Required)

Route	Feature requise
/api/cells	auth seulement
/api/kpi/summary	auth + kpis_basic
/api/kpi/{cell_id}	auth + kpis_basic
/api/drivetest	auth + kpis_basic
/api/outages	auth + kpis_basic
/api/heatmap	auth + heatmap
/api/son/events	auth + son
/api/export/csv	auth + export_csv
/api/simulate-outage	auth + son
/api/resolve-outage/{id}	auth + son
Tests validés (27/09)
Test	Résultat
POST /api/auth/signup (test@test.com)	✅ 201 + JWT
POST /api/auth/login	✅ 200 + JWT
GET /api/auth/me	✅ 200 (profil retourné)
GET /api/cells	✅ 200 (tenant_id: 1, count: 54)
GET /api/kpi/summary	✅ 200 (54 KPIs)
GET /api/son/events	❌ 402 (feature 'son' non incluse dans trial)
GET /api/heatmap	❌ 402 (feature 'heatmap' non incluse dans trial)
Dépendances ajoutées
text
sqlalchemy
psycopg[binary]
alembic
python-dotenv
passlib[bcrypt]
bcrypt==4.0.1          ← Version épinglée (bcrypt 5.x incompatible avec passlib)
python-jose[cryptography]
pydantic-settings
pydantic[email]
python-multipart
⚠️ Note critique : bcrypt 5.0.0 est incompatible avec passlib 1.7.4. Il faut épingler bcrypt==4.0.1 dans requirements.txt.

Points de vigilance
Dossier de travail : C:\Dev\rf-engineering-2-0\ (HORS OneDrive pour éviter les conflits de fichiers virtuels)

Venv : C:\Dev\rf-engineering-2-0\backend\venv\

.env contient : DATABASE_URL (Neon) et SECRET_KEY (JWT)

.env ne doit JAMAIS être commité (déjà dans .gitignore)

Doublon à surveiller : ne pas confondre app/routers/cells.py (routes) et app/models/cell.py (modèle)

Prochaines étapes — PHASE 3 : Frontend
□ Page /login HTML (formulaire email/password)
□ Stockage du JWT côté client (localStorage ou cookie)
□ Requêtes API avec header Authorization: Bearer <token>
□ Dashboard qui n'affiche que les données du tenant connecté
□ Gestion des erreurs 401 (redirection login) et 402 (message "upgrade ton plan")
PHASE 5 — Stripe (à venir)
□ Intégration Stripe Checkout
□ Webhooks Stripe (checkout.session.completed, customer.subscription.*)
□ Gestion des abonnements en DB
□ Page /billing avec bouton "Changer de plan"
Commandes utiles
Démarrer le serveur local :

powershell
cd C:\Dev\rf-engineering-2-0\backend
.\venv\Scripts\Activate.ps1
uvicorn main:app --reload --port 8000
Documentation interactive (Swagger) :

text
http://127.0.0.1:8000/docs
Tester les imports :

powershell
python -c "from app.main import app; print('App OK')"
Vérifier les tables Neon :

powershell
python -c "from app.database import engine; from sqlalchemy import inspect; print(inspect(engine).get_table_names())"
Créer les tables (si supprimées) :

powershell
python -c "from app.database import engine; from app.models import Base; Base.metadata.create_all(bind=engine)"
text

---

## 🎯 Étape 3 — Sauvegarde et publie

**1.** Sauvegarde (`Ctrl + S`) dans VS Code

**2.** Dans PowerShell :
```powershell
cd "C:\Users\Utilisateur\OneDrive\Escritorio\Nouveau Coulou\Mon site"
powershell
git add PASSATION.md
powershell
git commit -m "PASSATION: ajout section 14 (Phase 2 terminee)"
powershell
git pull
powershell
git push
---

## 15. Mise à jour du 28 septembre 2026 — PHASE 3 : FRONTEND & AUTH

### Statut : PHASE 3 TERMINÉE ✅ (local + Render)

### Authentification côté client

**Fichiers créés/modifiés :**
- `frontend/login.html` — Page de connexion (email + password)
- `frontend/js/auth.js` — Helpers JWT + authFetch
- `frontend/index.html` — Dashboard protégé par auth

**`frontend/js/auth.js` — Fonctions exposées :**

| Fonction | Rôle |
|---|---|
| `saveToken(t)` | Stocke le JWT dans localStorage (`rf_token`) |
| `getToken()` | Récupère le JWT |
| `clearToken()` | Efface le JWT (logout) |
| `isLoggedIn()` | Vérifie la présence d'un token |
| `login(username, password)` | POST /api/auth/login |
| `logout()` | Efface le token + redirect /login.html |
| `authFetch(url, options)` | Wrapper fetch avec Authorization: Bearer |
| `fetchMe()` | GET /api/auth/me |

### `authFetch` — Gestion des erreurs

| Code | Comportement |
|---|---|
| **200** | Retourne `res` normalement |
| **401** | `clearToken()` + redirect `/login.html` |
| **402** | Bannière "upgrade plan" (6s) + throw Error |
| **403** | (WebSocket uniquement) |

### WebSocket authentifié

Le JWT est passé en **query string** dans l'URL WebSocket :

```javascript
const WS_URL = (location.protocol === 'https:' ? 'wss://' : 'ws://')
  + location.host + '/ws/kpi'
  + (getToken() ? '?token=' + getToken() : '');
  
Si le token est absent → backend refuse (403).

### UI Header (dashboard)

Nouveaux éléments dans `.hdr-right` :
- `#userEmail` — Email de l'utilisateur (via `/api/auth/me`)
- `#logoutBtn` — Bouton Logout (clearToken + redirect login)

### Fichiers de configuration

- `backend/requirements.txt` — Complété avec les dépendances Phase 2 :
  sqlalchemy, psycopg[binary], alembic, python-dotenv, passlib[bcrypt],
  bcrypt==4.0.1, python-jose[cryptography], pydantic-settings,
  pydantic[email], python-multipart

- `backend/app/main.py` — `media_type="text/html; charset=utf-8"` ajouté sur les routes `/`, `/login.html`, `/signup.html` (fix accents)

### Variables d'environnement Render

**Ajoutées sur Render (Environment) :**
- `DATABASE_URL` — Connection string Neon (avec `+psycopg`)
- `SECRET_KEY` — Clé JWT (identique au `.env` local)

⚠️ Sans ces variables, Render crash au démarrage : `ValueError: DATABASE_URL manquant dans env`

### Tests validés (28/09)

| Test | Résultat |
|---|---|
| Login `boss@rfboss.com` / local | ✅ 200 + JWT |
| Login `boss@rfboss.com` / Render | ✅ 200 + JWT |
| Dashboard local avec auth | ✅ LIVE, 54 cellules |
| Dashboard Render avec auth | ✅ LIVE, 54 cellules |
| Logout (clic bouton) | ✅ Redirect /login.html |
| Accents UTF-8 (KPI RÉSEAU) | ✅ Propres |
| Bannière 402 sur Heatmap (trial) | ✅ Affichée |
| WebSocket avec token | ✅ Connecté |

### Commits clés (repo rf-engineering-2-0)


### Points de vigilance

1. **Encodage** : NE JAMAIS utiliser PowerShell `Set-Content`/`WriteAllText` sur des fichiers HTML/Python. Utiliser **VS Code** (UTF-8 sans BOM).
2. **`git restore`** : écrase les modifs locales. Toujours commiter avant.
3. **`.env` local** : contient `DATABASE_URL` + `SECRET_KEY`. Jamais commité.
4. **Render Environment** : si on régénère `SECRET_KEY`, tous les JWT existants deviennent invalides.
5. **Comptes de test** : `boss@rfboss.com` / `Boss1234!` (tenant `rfboss`, plan trial).

### Prochaines étapes — PHASE 4 : Onboarding & plans

- [ ] Page `/signup.html` dédiée
- [ ] Validation côté client (email, mot de passe)
- [ ] Choix du plan à l'inscription
- [ ] Badge du plan dans le header
- [ ] Message clair quand quota atteint

### PHASE 5 — Stripe (à venir)

- [ ] Stripe Checkout
- [ ] Webhooks
- [ ] Table `subscriptions` en DB
- [ ] Basculement trial → starter/pro

---

## 16. Mise à jour du 28 septembre 2026 — PHASE 4 + PROTECTION JURIDIQUE

### Statut : PHASE 4 TERMINÉE À 90% (4.5 reportée)

### A. Protection juridique Knowledge Base (12 pages)

**Contexte :** Audit des 12 pages HTML du dossier `knowledge/` pour anticiper tout risque lié aux marques et paramètres constructeurs (Ericsson, Nokia, Huawei, Samsung).

**Actions réalisées :**

- **`LICENSE` mis à jour** — ajout d'une note "third-party trademarks" qui précise que les marques citées appartiennent à leurs propriétaires respectifs et que leur mention est informative uniquement.
- **Script Python `add_disclaimers.py` créé** (à la racine de `Mon site/`) — ajoute automatiquement à chaque page `knowledge/*.html` :
  - Un **bandeau "Avertissement légal"** après `<body>` (ou après `</nav>` pour les pages à nav fixe)
  - Une **section "Sources et références"** avant `<footer>`
  - Le script est **idempotent** (peut être relancé sans dupliquer).
- **Pages patchées :** 5g-nr, context-caribbean, drive-test, ericsson, huawei, index, interferences, mapping, nokia, planning-rf, samsung, tdd-fdd (12/12).
- **Fix layout grid** — les pages en `display:grid` recevaient le bandeau dans la sidebar. Correction : `grid-column:1/-1` sur le bandeau.
- **Fix index.html** — le bandeau était caché par la nav fixe. Correction : déplacé après `</nav>` avec `margin:64px 0 0 0`.

**Commits poussés (repo portfolio) :**
- `b75a15c1` — Legal: disclaimers + sources sur les 12 pages knowledge
- `46f4b36` — Fix: bandeau plein-largeur (grid-column) sur pages knowledge

---

### B. Phase 4 — Onboarding & Plans (Dashboard SaaS)

#### 4.1 — Page signup.html

**Fichier créé :** `frontend/signup.html`

**Fonctionnalités :**
- Formulaire : email + nom complet + nom entreprise + password + confirmation
- **Slug auto-généré** depuis le nom d'entreprise (slugify client-side : minuscules, accents retirés, tirets)
- Validation client (passwords matchent, longueur ≥ 8)
- Appel `POST /api/auth/signup` avec la structure `{payload: {...}, tenant_data: {...}}`
- Sauvegarde du token + redirect dashboard

#### 4.2 — Badge du plan dans le header

**Backend modifié :**
- `backend/app/schemas/user.py` — `UserRead` étendu avec `plan: Optional[str]` et `tenant_name: Optional[str]`
- `backend/app/routers/auth.py` — la route `/me` joint maintenant `Tenant` et enrichit la réponse avec `plan` et `tenant_name`

**Frontend modifié :** `frontend/index.html`
- Ajout `<span id="planBadge" class="plan-badge">` dans `user-box`
- CSS : 4 variantes de couleur (trial gris, starter cyan, pro violet, enterprise or)
- JS : `loadUserInfo()` récupère `user.plan` et applique la classe correspondante

#### 4.3 — Lock visuel des features par plan

**Frontend modifié :** `frontend/index.html`

**Mécanisme :**
- Constante `PLAN_FEATURES` (objet JS) qui définit les features par plan :
  - `trial` : kpis_basic, map
  - `starter` : + son, export_csv
  - `pro` : + heatmap, self_healing
  - `enterprise` : `*` (tout)
- Fonction `hasFeature(plan, feature)` et `applyPlanLock(plan)` qui :
  - Ajoute la classe `locked` aux boutons non accessibles → grisés + icône 🔒
  - Retire la classe `active` pour éviter la bordure bleue trompeuse
  - **Masque le panneau SON de droite** si le plan n'a pas accès à `son`
- Les boutons restent **cliquables** → permet au 402 banner de Phase 3 de s'afficher (message "upgrade plan")

#### 4.4 — Page /billing

**Fichier créé :** `frontend/billing.html`
**Route ajoutée :** `backend/app/main.py` → `@app.get("/billing.html")`

**Contenu :**
- Bloc "Plan actuel" (nom du tenant + plan + badge coloré)
- 4 cartes de plans (Trial/Starter/Pro/Enterprise) avec features ✓/✗
- Carte du plan actuel surlignée + bouton grisé "Plan actuel"
- Boutons "Choisir" → placeholder (alert "arrive bientôt" avant intégration Stripe)
- Bouton "Nous contacter" pour Enterprise → ouvre mailto
- **Lien** : badge `TRIAL` dans le header du dashboard devient cliquable → redirige vers `/billing.html`

#### 4.5 — Message quota sites/users

**Statut : NON IMPLÉMENTÉE.**

**Raison :** aucune route `POST /api/sites` ni `POST /api/users` n'existe encore dans le backend. Sans possibilité de créer des sites ou users, aucun quota ne peut être atteint.

**Décision reportée** — 3 options ouvertes :
- **B1** : créer les routes sites/users + quotas (prépare Phase 5 Stripe)
- **B2** : passer directement à Stripe (mais vendre un plan qui n'ajoute pas de features réelles est prématuré)
- **B3** : reporter

---

### FIX CRITIQUE (découvert pendant Phase 4.4)

**Problème :** `app.mount("/static", StaticFiles(...))` dans `main.py` était **mal indenté** — il était placé à l'intérieur de la fonction `billing_page()`, donc exécuté uniquement à l'accès de `/billing.html`. Résultat : `/static/js/auth.js` retournait **404** en permanence, cassant tout le dashboard (erreur `authFetch is not defined`).

**Fix :** désindenter la ligne `app.mount(...)` pour qu'elle soit au niveau du `if FRONTEND_DIR.exists():`.

**Leçon :** toujours vérifier l'indentation des `app.mount()` et autres décorateurs FastAPI. Un seul niveau d'indentation en trop peut désactiver toute une route.

---

### Commits poussés (repo rf-engineering-2-0)

| Commit | Description |
|---|---|
| `65d5f74` | Phase 4.1-4.2 : signup.html + badge plan dans le header |
| `18b6bdbc` | Phase 4.4 : page billing + fix app.mount() indentation |

---

### Points de vigilance Phase 4

1. **app.mount() / décorateurs FastAPI** — toujours vérifier l'indentation au même niveau que `if FRONTEND_DIR.exists():`
2. **Uvicorn --reload** ne détecte pas toujours les changements de fichiers statiques (`frontend/*.html`). Un redémarrage manuel (`Ctrl+C` puis relance) est parfois nécessaire.
3. **Cache Chrome** — les 404 et erreurs JS restent cachés. Tester en **incognito** (`Ctrl+Shift+N`) pour diagnostiquer.
4. **Le script `add_disclaimers.py`** doit être relancé si on ajoute de nouvelles pages `knowledge/*.html`.
5. **Le badge plan** dépend du backend `/me` — si on modifie `UserRead`, vérifier que `plan` et `tenant_name` sont toujours renvoyés.

---

### Prochaines étapes — PHASE 5 : Stripe (à venir)

**Prérequis :**
- Créer les routes `POST /api/sites` et `POST /api/users` (quota)
- Créer la table `subscriptions` en DB
- Intégration Stripe Checkout (bouton "Upgrade" sur `/billing.html`)
- Webhook `checkout.session.completed` → maj `tenant.plan` en DB
- Page `/billing/portal` pour gérer l'abonnement

**Décision à prendre :**
- **B1** : routes sites/users + quotas d'abord, Stripe ensuite
- **B2** : Stripe direct (nécessite de simuler les features)
- **B3** : reporter