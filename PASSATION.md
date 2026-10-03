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

---

## 17. Mise à jour du 29 septembre 2026 — PHASE 5 : STRIPE (en cours)

### Statut : 70% — Checkout OK, Webhook à débugger

### Ce qui est fait

**Compte Stripe** : créé, en mode TEST (bac à sable)
- Compte : Groupe Jean Thomas Montreuil
- Sandbox : Bac à sable de Jean Thomas Montreuil Group
- Account ID : `acct_1UL3EWBUAqbxmmG4`

**Produits Stripe créés** :
| Produit | Prix | Price ID |
|---|---|---|
| RF Engineering Starter | 490 $ CAD/mois | `price_1UL3aGBUAqbxmmG4UKsUMDTQ` |
| RF Engineering Pro | 1490 $ CAD/mois | `price_1UL3buBUAqbxmmG4pAD2Hrxs` |

**Fichiers backend créés** :
- `app/services/stripe_service.py` — `create_checkout_session()` + `construct_webhook_event()`
- `app/routers/billing.py` — `POST /api/billing/checkout` + `POST /api/billing/webhook`

**Fichiers frontend modifiés** :
- `frontend/billing.html` — bouton "Choisir Starter/Pro" appelle `/api/billing/checkout` et redirige vers Stripe Checkout
- `backend/app/main.py` — inclusion du router billing

**Variables d'environnement ajoutées à `.env`** :
STRIPE_SECRET_KEY=sk_test_...
STRIPE_PUBLISHABLE_KEY=pk_test_...
STRIPE_PRICE_STARTER=price_1UL3aG...
STRIPE_PRICE_PRO=price_1UL3bu...
STRIPE_WEBHOOK_SECRET=whsec_...


**Stripe CLI installé** :
- Fichier : `C:\Dev\stripe.exe`
- Login : OK (account acct_1UL3EWBUAqbxmmG4)
- Tunnel actif : `C:\Dev\stripe.exe listen --events checkout.session.completed,customer.subscription.deleted --forward-to http://127.0.0.1:8000/api/billing/webhook`

### Ce qui marche

- ✅ `POST /api/billing/checkout` → retourne une URL Stripe Checkout valide
- ✅ Page Stripe Checkout s'ouvre (490 $ CAD, carte de test 4242 acceptée)
- ✅ Paiement accepté en test → redirect `?checkout=success`
- ✅ Webhook arrive bien au backend (`POST /api/billing/webhook`)

### Ce qui ne marche PAS

- ❌ Le webhook renvoie **400 Bad Request** — `construct_webhook_event` échoue
- ❌ Le plan du tenant **ne passe pas** de `trial` à `starter` après paiement
- ❌ Le badge dans le header reste TRIAL

### Diagnostic en cours

Le message d'erreur uvicorn était :WEBHOOK construct_error: 400: Signature invalide


Cause probable : **mismatch entre le whsec dans `.env` et celui du `stripe listen` actuel**. À vérifier.

### Commits poussés
c955f0a Phase 5: integration Stripe (checkout + webhook)


### Fichiers à ne PAS commiter (rappel)

- `backend/.env` (contient les clés sk_test et whsec)
- Doit être dans `.gitignore` (déjà fait)

### Pour reprendre la prochaine session

**1.** Vérifier que `STRIPE_WEBHOOK_SECRET` dans `.env` = celui affiché par `stripe listen`

**2.** Redémarrer uvicorn après toute modif `.env`

**3.** Lancer un trigger de test : `C:\Dev\stripe.exe trigger checkout.session.completed`

**4.** Regarder les logs uvicorn (les `logger.info("WEBHOOK ...")` sont en place)

**5.** Une fois que le webhook renvoie **200 OK** → faire un vrai paiement test 4242 → vérifier que le badge passe à STARTER

### Points de vigilance

- **Ne JAMAIS** mettre les clés Stripe en dur dans le code — toujours via `.env`
- **Ne JAMAIS** committer `.env`
- Le `whsec_` change **à chaque redémarrage** de `stripe listen` → si les tests échouent, vérifier qu'il est à jour dans `.env`
- Uvicorn **ne recharge pas** `.env` automatiquement → redémarrage manuel nécessaire
- **3 terminaux obligatoires** : `stripe listen`, `uvicorn`, `terminal de commandes`

### Prochaine étape après Phase 5

- Phase 6 — Opérations (monitoring, backup, support client)
- Ou passe en **production** Stripe (vraies clés `sk_live_`, `pk_live_`, vrais price IDs)
- Ou premier client payant en pilote


---

## 18. Mise à jour du 29 septembre 2026 — PHASE 5 : STRIPE TERMINÉE ✅

### Statut : SaaS fonctionne end-to-end (local)

### Test end-to-end validé

Signup → Login → Dashboard → Cliquer "Choisir Starter" → Stripe Checkout → Paiement 4242 → Webhook → Plan mis à jour → Features débloquées automatiquement.

Le compte `admin@rfboss.com` est passé de TRIAL à STARTER après un paiement test Stripe.

### Changement majeur : nouveau projet Neon

L'ancien projet Neon (rf-engineering, Ohio) avait un problème récurrent de mot de passe. On l'a abandonné.

Nouveau projet Neon :
- Nom : rf-engineering-2
- Région : AWS US East 2 (Ohio)
- Les credentials sont dans backend/.env (jamais commités)

### Comptes de test locaux

| Email | Mot de passe | Plan | Tenant |
|---|---|---|---|
| admin@rfboss.com | Admin1234! | STARTER | RF Boss |
| test2@rfboss.com | (perdu - ancien Neon) | - | - |

### Fichiers backend modifiés (commit 8a47952)

- app/database.py - ajout load_dotenv(override=True)
- app/services/stripe_service.py - construct_webhook_event avec bypass signature si STRIPE_DEV_MODE=1
- app/routers/billing.py - fix to_dict() pour stripe-python v15 + logs détaillés

### Commandes utiles (local)

Terminal 1 - Uvicorn :
    cd C:\Dev\rf-engineering-2-0\backend
    .\venv\Scripts\Activate.ps1
    uvicorn main:app --reload --port 8000

Terminal 2 - Stripe webhook tunnel (à laisser tourner) :
    C:\Dev\stripe.exe listen --events checkout.session.completed,customer.subscription.deleted --forward-to http://127.0.0.1:8000/api/billing/webhook

Tuer uvicorn :
    taskkill /F /IM python.exe

### Points de vigilance CRITIQUES

1. Ne JAMAIS utiliser PowerShell pour écrire dans .env - provoque des corruptions. Utiliser Notepad ou VS Code en UTF-8.

2. Uvicorn ne recharge PAS .env automatiquement. Après toute modif : taskkill /F /IM python.exe puis relance.

3. +psycopg obligatoire dans DATABASE_URL (sinon SQLAlchemy cherche psycopg2 non installé).

4. &channel_binding=require à la fin de l'URL Neon peut poser problème avec psycopg v3. Retirer si besoin.

5. STRIPE_DEV_MODE=1 bypass la vérification de signature webhook. À RETIRER en production.

6. Neon Free Tier : cold start 10-30s après inactivité.

7. .env ne doit JAMAIS être commité (déjà dans .gitignore).

8. app.mount("/static", ...) doit être indenté au même niveau que if FRONTEND_DIR.exists(): - sinon 404 sur tous les assets.

9. GitHub Secret Scanning bloque tout push contenant des clés Stripe (sk_test_...) ou des mots de passe Neon (npg_...). Ne jamais les mettre dans PASSATION.md.

### À FAIRE - PROCHAINE SESSION

#### 1. Mettre à jour Render (10 min)

Le compte admin@rfboss.com n'existe PAS sur Render (ancien Neon abandonné).

Actions :
1. https://dashboard.render.com → service rf-engineering-2-0 → Environment
2. Mettre à jour DATABASE_URL avec la nouvelle URL Neon (avec +psycopg)
3. Vérifier SECRET_KEY
4. Vérifier STRIPE_SECRET_KEY, STRIPE_PUBLISHABLE_KEY
5. Ajouter STRIPE_PRICE_STARTER, STRIPE_PRICE_PRO, STRIPE_WEBHOOK_SECRET
6. NE PAS ajouter STRIPE_DEV_MODE en prod
7. Save Changes → attendre redéploiement (2-3 min)
8. Aller sur https://rf-engineering-2-0.onrender.com/signup.html → créer un compte prod

#### 2. Retirer STRIPE_DEV_MODE=1 avant la prod

En production, la vérification de signature webhook doit être active.

#### 3. Passer Stripe en production (quand tu as un vrai client)

- Créer les produits en mode live sur Stripe
- Régénérer les clés sk_live_, pk_live_
- Créer un nouveau webhook endpoint pour l'URL de prod
- Copier le nouveau whsec_... dans les variables Render
- Mettre à jour STRIPE_PRICE_STARTER, STRIPE_PRICE_PRO avec les IDs live

#### 4. Sécurité - régénérer les clés exposées

Pendant le debug, plusieurs secrets ont été partagés dans le chat :
- Clé Stripe test sk_test_...
- Mot de passe Neon npg_...

Actions recommandées :
- Stripe : Développeurs → Clés API → Roll key (régénérer)
- Neon : Console → projet → Reset password

### Commits clés de la session

    8a47952 Phase 5: Stripe end-to-end fonctionnel (checkout + webhook)
    c955f0a Phase 5: integration Stripe (checkout + webhook)
    155e60d Phase B: page sites.html + indicateur quota header
    34e1078 Phase 4.5: routes sites/users + quotas par plan (402)

### Leçon de la session

PowerShell est un piège pour éditer des fichiers de config avec des valeurs sensibles. Toujours utiliser Notepad ou VS Code.

Toujours tester la connexion DB séparément avant de lancer uvicorn.


---

## 19. Mise à jour du 30 septembre 2026 — SaaS EN LIGNE via Cloudflare Tunnel

### Statut : SaaS accessible publiquement ✅

### Solution retenue : Cloudflare Tunnel

Après avoir échoué sur :
- **Render Free** (refus de connexion à Neon — IP partagées bloquées)
- **Oracle Cloud ARM** (Out of capacity permanent sur AD-1/AD-2/AD-3)
- **Fly.io** (carte de crédit requise à l'inscription)

La solution qui marche : **Cloudflare Tunnel** + uvicorn en local.

**URL publique** : `https://xxx-xxx-xxx.trycloudflare.com` (change à chaque redémarrage)

### Comment ça marche

Cloudflare Tunnel crée un tunnel HTTPS public vers le localhost. Le PC reste le serveur, Cloudflare s'occupe du DNS + HTTPS.

**2 terminaux obligatoires :**

**Terminal 1 — Uvicorn** :

cd C:\Dev\rf-engineering-2-0\backend
.\venv\Scripts\Activate.ps1
uvicorn main:app --reload --port 8000


**Terminal 2 — Cloudflare Tunnel** :

cloudflared tunnel --url http://localhost:8000

→ Copie l'URL `https://xxx.trycloudflare.com` affichée et ouvre-la dans Chrome.

### Installation (faite une seule fois)

winget install --id Cloudflare.cloudflared


### Avantages / Limites

| Avantage | Limite |
|---|---|
| Gratuit, aucune carte | PC doit rester allumé |
| HTTPS automatique | URL change à chaque redémarrage |
| Pas de cold start | Pas de vrai domaine (pour l'instant) |
| Marche avec Neon + Stripe | |

### Pour une URL fixe (à faire quand tu auras un domaine)

Cloudflare propose des **tunnels nommés** avec un domaine custom (~10$/an) :
1. Acheter un domaine (Namecheap, Cloudflare)
2. Configurer un tunnel nommé dans Cloudflare Zero Trust
3. URL fixe : `https://rf.ton-domaine.com`

### Test validé ce soir

- ✅ Login `admin@rfboss.com` / `Admin1234!` via URL Cloudflare
- ✅ Dashboard LIVE, badge STARTER, 54 cellules
- ✅ SON Actions temps réel
- ✅ Quota sites 0/10

### Alternatives éliminées (à ne pas retenter)

| Solution | Raison de l'échec |
|---|---|
| Render Free | IP partagées bloquées par Neon |
| Render Starter (7$/mois) | Pas de budget pour l'instant |
| Oracle Cloud ARM | Out of capacity chronique |
| Fly.io | Carte de crédit obligatoire |
| Vercel | Pas adapté pour FastAPI+WebSocket |

### Prochaines étapes (quand budget/domaine dispo)

1. Acheter un domaine (~10$/an)
2. Configurer Cloudflare Tunnel nommé → URL fixe
3. OU passer à Render Starter (7$/mois) quand budget le permet
4. OU retenter Oracle Cloud tôt le matin (5h-7h)

⚠️ Vérifie qu'il n'y a AUCUN secret dans ce que tu colles (pas de sk_test_, pas de npg_, pas de whsec_, pas de clé SSH).

Ctrl + S → ferme Notepad

---

## 20. Mise à jour du 1er octobre 2026 — Portfolio mobile + Vidéo démo + Jobs v4

### Statut : Portfolio responsive ✅ + Démo vidéo ✅ + Jobs v4 ✅

### A. Portfolio responsive mobile

**Problème :** sur téléphone, la barre de navigation débordait et aucun menu n'était accessible sauf "Contact".

**Solution :** menu hamburger responsive + corrections mobile.

**Modifications dans `index.html` :**
- Ajout d'un bouton `.menu-toggle` (☰) caché sur desktop
- Media query @900px : le menu devient vertical et s'ouvre au clic
- JavaScript pour ouvrir/fermer le menu
- Corrections responsive supplémentaires à @600px (padding, grilles, stats)
- Bug fix : balise `</div>` manquante dans la section News

**Fichiers touchés :**
- `index.html` (nav + CSS + JS)

### B. Vidéo démo RF Engineering 2.0

**Objectif :** démontrer le SaaS en attendant un domaine propre.

**Outils utilisés :**
- **Playwright** (Python) → enregistrement automatisé de l'écran
- **edge-tts** (Microsoft) → voix off française
- **ffmpeg** → fusion vidéo + audio

**Fichiers créés :**
- `demo_recorder.py` → script Playwright qui enregistre 7 scènes du dashboard
- `voice_over.py` → génère la voix + fusionne avec la vidéo
- `videos_demo/` → dossier des vidéos brutes `.webm`
- `demo_rf_engineering.mp4` → vidéo finale avec voix off

**Configuration voix :**
- `VOICE = "fr-FR-HenriNeural"` (voix masculine française, professionnelle)

**Résultat :**
- Vidéo de ~1min22 avec voix off masculine
- Uploadée sur YouTube en **Non répertorié** : `nHXvM27dTa0`
- Intégrée dans le portfolio via une **modale HTML** avec iframe

**Modifications dans `index.html` :**
- Lien "🎬 Voir la démo vidéo" dans la carte RF Engineering 2.0
- Modale avec iframe YouTube
- CSS + JS pour l'ouverture/fermeture (Échap + clic extérieur)

### C. Jobs v4 — 2 catégories RF + Admin

**Contexte :** le marché canadien RF est difficile sans OIQ. Besoin d'un filet de sécurité avec des jobs administratifs/support.

**Solution :** refonte complète du système de veille d'emploi en 2 onglets.

**Fichiers créés/modifiés :**

| Fichier | Rôle |
|---|---|
| `fetch_jobs_v4.py` | Script principal (remplace v3) |
| `fetch_jobs.py` | Copie de v4 (utilisée par GitHub Actions) |
| `fetch_jobs_v3_OLD.py` | Ancien script (backup) |
| `jobs.html` | Refonte complète avec 2 onglets |
| `jobs.json` | Sauvegarde RF + Admin séparées |
| `jobs_BACKUP_*.html` | Backups automatiques |

**Structure des 2 onglets :**

| Onglet | Contenu | Source |
|---|---|---|
| 📡 RF & Télécom | ~246 offres | Adzuna + Remotive |
| 💼 Missions & Support | ~46 offres | Adzuna (Chicoutimi/Saguenay uniquement) |

**Mots-clés RF :** identiques à v3 + 16 mots-clés élargis

**Mots-clés Admin (Chicoutimi/Saguenay) :**
- FR : agent administratif, commis de bureau, secrétaire, réceptionniste, service à la clientèle, livreur, magasinier, manutentionnaire, caissier, préposé...
- EN : receptionist, clerk, warehouse worker, delivery driver, cashier...

**Scoring intelligent :**
- **RF** : scoring v3 (pénalité étudiant, bonus senior)
- **Admin** : scoring simple basé sur mots-clés + bonus localisation Chicoutimi/Saguenay (+25pts)
- Filtre admin : score minimum 10/100

**Nouveau : Bouton "📋 Préparer"**

Sur chaque offre avec score ≥ 50, un bouton permet de :
1. Télécharger un fichier `offre_XXX.txt` au format `manual_offer.txt`
2. Copier ce fichier dans le dossier `Mon site/` en le renommant `manual_offer.txt`
3. Lancer `python prepare_manual.py` → 3 documents générés (CV + lettre + prépa)

**Format du fichier téléchargé :**
TITLE: <titre>
COMPANY: <entreprise>
LOCATION: <lieu>
URL: <lien>

DESCRIPTION:
<description complète>


### D. Marqueurs HTML pour injection automatique

Pour éviter la corruption du HTML à chaque exécution (comme dans l'ancienne version), on utilise maintenant des **marqueurs** :

```html
<!-- RF_JOBS_START -->
...
<!-- RF_JOBS_END -->

<!-- ADMIN_JOBS_START -->
...
<!-- ADMIN_JOBS_END -->

---

## 22. Nouveau projet : RF Analytics (2 octobre 2026)

### Statut : Backend initial fonctionnel ✅

**RF Analytics** est un nouveau produit SaaS séparé de RF Engineering 2.0, vendu indépendamment.

**Positionnement :** "Le copilote du manager RF" — Tableaux de bord historiques, bulletins de santé réseau, alertes intelligentes.

**Repo :** https://github.com/mmjt2000/rf-analytics (privé)

**Stack :** FastAPI + PostgreSQL + TimescaleDB + Docker

**Structure initiale créée :**
- backend/app/ (modèles, services, routers, workers, templates)
- frontend/ (HTML/CSS/JS)
- docker-compose.yml (PostgreSQL + TimescaleDB)
- 5 tables : tenants, users, kpi_history, bulletins, alerts

**Prochaine étape :** authentification JWT + multi-tenancy

---

## 23. Mise à jour du 2 octobre 2026 — RF Analytics : Backend complet

### Statut : Backend multi-tenant + pipeline d'ingestion opérationnels ✅

### A. Nouveau repo créé

**Repo GitHub :** https://github.com/mmjt2000/rf-analytics (privé)
**Dossier local :** `C:\Dev\rf-analytics`

### B. Structure du projet (44+ fichiers)
rf-analytics/
├── backend/
│ ├── app/
│ │ ├── main.py ← Point d'entrée FastAPI
│ │ ├── config.py ← Chargement .env
│ │ ├── database.py ← SQLAlchemy + PostgreSQL
│ │ ├── dependencies.py ← JWT get_current_user
│ │ ├── models/ ← 5 modèles SQLAlchemy
│ │ ├── schemas/ ← Pydantic (user, tenant, kpi)
│ │ ├── services/ ← auth, tenant, ingestion
│ │ ├── routers/ ← auth, kpis
│ │ ├── workers/ ← ingestion_worker
│ │ └── templates/ ← bulletin.html
│ └── requirements.txt
├── frontend/ ← (vide pour l'instant)
├── scripts/init_db.sql ← Création des 5 tables
├── docker-compose.yml ← db + backend + worker
├── Dockerfile ← python:3.12-slim-bookworm
└── .env ← Local (gitignored)


### C. Tables PostgreSQL + TimescaleDB

| Table | Rôle | Statut |
|---|---|---|
| `tenants` | Multi-tenancy + branding | ✅ |
| `users` | Utilisateurs (JWT) | ✅ |
| `kpi_history` | **Hypertable TimescaleDB** | ✅ |
| `bulletins` | Bulletins de santé (à venir) | ✅ |
| `alerts` | Alertes intelligentes (à venir) | ✅ |

**Tenant par défaut :** `Digicel Haïti` (id=1, slug `digicel-ht`)

### D. Authentification JWT

**Routes actives :**
| Route | Méthode | Description |
|---|---|---|
| `/api/auth/signup` | POST | Créer tenant + admin |
| `/api/auth/login` | POST | Obtenir un JWT |
| `/api/auth/me` | GET | Profil (protégé) |

**Compte de test :**
- Email : `admin@test.com`
- Mot de passe : `Test1234!`
- Tenant : `Test Réseau` (id=1)

**Sécurité :**
- bcrypt==4.0.1 (épinglé — bcrypt 5.x incompatible avec passlib)
- JWT HS256, expiration 24h
- `SECRET_KEY` dans `.env`

### E. API KPI (nouvelles routes)

| Route | Méthode | Description |
|---|---|---|
| `/api/kpis/summary` | GET | Agrégation sur N heures |
| `/api/kpis/history` | GET | Historique paginé |
| `/api/kpis/cell/{cell_id}` | GET | KPI d'une cellule |
| `/api/kpis/top-sites` | GET | Top/Flop cellules |

Toutes protégées par JWT + filtre par `tenant_id`.

### F. Pont RF Engineering → RF Analytics

**Côté RF Engineering 2.0 :** Nouvelle route `/api/export/kpis` dans `backend/app/routers/export.py`

- Authentification : Header `X-API-Key`
- Clé partagée : `shared-secret-rf-analytics-2026` (dans `.env` des 2 projets)
- Retourne : liste des 54 cellules avec tous leurs KPI (format JSON)

**Côté RF Analytics :** Service d'ingestion `backend/app/services/ingestion_service.py`

- Appelle `RF_ENGINEERING_URL/api/export/kpis` via httpx
- Stocke dans `kpi_history` (TimescaleDB)
- URL locale : `http://host.docker.internal:8000` (Docker → PC Windows)

### G. Worker automatique

**Fichier :** `backend/app/workers/ingestion_worker.py`

- Boucle infinie, **intervalle 300 secondes** (5 min)
- Ingère pour les tenants listés dans `TENANTS_TO_INGEST = [1]`
- Tourne comme **service séparé** dans docker-compose
- Logs : `docker compose logs worker`

**Test validé :** 7 cycles × 54 cellules = **378 lignes** dans `kpi_history`

### H. Résultats de test

```powershell
# Test /api/kpis/summary (heures=24)
tenant_id          : 1
total_cells        : 54
total_samples      : 378
avg_health         : 87.24
avg_rsrp           : -89.18
avg_sinr           : 14.03
avg_dl_throughput  : 39.78
avg_drop_call_rate : 0.0083
avg_rrc_setup_sr   : 98.53
avg_prb_util       : 0.5937

 Corrections importantes
1. Dockerfile : python:3.12-slim ne fonctionne PAS

Erreur : Playwright ne trouve pas les paquets Debian 13 (Trixie)

Solution : utiliser python:3.12-slim-bookworm (Debian 12 stable)

2. Uvicorn côté RF Engineering :

Par défaut : écoute sur 127.0.0.1 (inaccessible depuis Docker)

Obligatoire : --host 0.0.0.0 pour que le conteneur puisse l'appeler

3. .env ne se recharge PAS avec docker compose restart

Il faut docker compose up -d --force-recreate après modif du .env

4. Alignement tenant_id :

Le user admin@test.com peut être sur un tenant différent de celui ingéré

Corriger avec : UPDATE users SET tenant_id = 1 WHERE email = 'admin@test.com';

J. Commandes de démarrage
RF Analytics :
cd C:\Dev\rf-analytics
docker compose up -d
docker compose logs worker  # vérifier l'ingestion

RF Engineering 2.0 (en parallèle) :

cd C:\Dev\rf-engineering-2-0\backend
.\venv\Scripts\Activate.ps1
uvicorn main:app --reload --host 0.0.0.0 --port 8000

Accès :

RF Analytics API : http://localhost:8001/docs

RF Engineering API : http://127.0.0.1:8000/docs

K. Sécurité — À régénérer
⚠️ Clé Adzuna (exposée dans chat) → à régénérer sur https://developer.adzuna.com

⚠️ Clé Groq (exposée dans chat) → à régénérer sur https://console.groq.com

⚠️ Token GitHub (si partagé) → à régénérer

L. Prochaines étapes — Session suivante
Priorité 1 : Frontend RF Analytics (login + dashboard)
Priorité 2 : Service de bulletins PDF (killer feature)
Priorité 3 : Service d'alertes (détection anomalies)
Priorité 4 : Stripe Billing
Priorité 5 : Déploiement (Render ou Cloudflare Tunnel)

M. Notes importantes
Docker Desktop doit être lancé avant docker compose up

Le worker tourne en arrière-plan (500 MB RAM)

La base TimescaleDB compresse après 7 jours (policy à activer)

Multi-tenancy : tenant_id filtré automatiquement via get_current_tenant_id

text

---

## 🔹 Puis commit + push

Dans PowerShell :

```powershell
cd C:\Dev\rf-engineering-2-0
git add PASSATION.md
git commit -m "PASSATION: section 23 - RF Analytics backend complet + pipeline"
git push

---

## 24. Mise à jour du 3 octobre 2026 — RF Analytics : Bulletins PDF

### Statut : Killer feature opérationnelle ✅

### A. Nouveaux services

| Fichier | Rôle |
|---|---|
| `backend/app/services/analytics_service.py` | Agrégation des KPI (scores, breakdown, tendances) |
| `backend/app/services/bulletin_service.py` | Génération PDF via Jinja2 + Playwright |

### B. Nouvelles routes API

| Route | Méthode | Description |
|---|---|---|
| `/api/bulletins/generate` | POST | Génère un bulletin (retourne chemins) |
| `/api/bulletins/` | GET | Liste les bulletins existants |
| `/api/bulletins/download/{filename}` | GET | Télécharge un PDF |

### C. Template bulletin

- Fichier : `backend/app/templates/bulletin.html`
- ~347 lignes (HTML + CSS + Jinja2)
- Design multi-tenant (couleurs configurables par tenant)
- Sections : Score global, KPI, Tendance, Top problèmes, Top succès, Impact business

### D. Test validé

**Bulletin généré :**
- Health Score : **86/100**
- PDF : 265 Ko
- Nom : `bulletin_DigicelHaiti_20261003_165922.pdf`

### E. Corrections importantes

**1. `config.py` — `BASE_DIR` corrigé**
```python
# AVANT (mauvais) :
BASE_DIR = Path(__file__).parent.parent.parent

# APRÈS (correct) :
BASE_DIR = Path(__file__).parent.parent

Raison : config.py est dans backend/app/, donc parent.parent = backend/ (racine du projet).

2. Slugification des noms de fichiers

Problème : Digicel Haïti → accents (ï) cassaient les URLs

Solution : unicodedata.normalize("NFKD", ...) pour retirer les accents

Résultat : bulletin_DigicelHaiti_...pdf (sans tréma)

F. Docker — Accès aux fichiers générés
Volume monté : ./backend:/app → les PDFs sont directement accessibles sur le PC dans C:\Dev\rf-analytics\backend\bulletins\

Plus besoin de docker cp (qui bug sur Windows avec certains noms)

G. Commandes de test
powershell
# Générer un bulletin (via Swagger)
POST /api/bulletins/generate?hours=168

# Le PDF apparaît dans :
C:\Dev\rf-analytics\backend\bulletins\bulletin_*.pdf

# Ou télécharger via API :
GET /api/bulletins/download/bulletin_*.pdf
H. Prochaine session
Options :

🎨 Frontend RF Analytics (page login + dashboard)

🚨 Service d'alertes (détection anomalies)

📅 Scheduler (génération auto hebdo + envoi email)

💳 Stripe Billing

🚀 Déploiement (Cloudflare Tunnel + Render)

text

Puis :

```powershell
cd C:\Dev\rf-engineering-2-0
git add PASSATION.md
git commit -m "PASSATION: section 24 - bulletins PDF opérationnels"
git push
📋 Récapitulatif
#	Action	Statut
1	Commit + push rf-analytics	⏳
2	Update PASSATION.md	⏳
3	Commit + push rf-engineering-2-0	⏳
Fais les 3 étapes et dis-moi si tout est pushé. 🚀

Ensuite on peut :

🅰️ S'arrêter là (belle session)

🅱️ Continuer avec une autre fonctionnalité

Excellent boulot, amigo ! 🎉

The user pushed successfully. The commit was "Feature: génération de bulletins PDF + API download" and it succeeded (3d1ee2..4e81181 main -> main). Now let's update the PASSATION.md.

🎉 Commit + push réussis !

text
[main 4e81181] Feature: génération de bulletins PDF + API download
 7 files changed, 1439 insertions(+)

To https://github.com/mmjt2000/rf-analytics.git
   3d1ee2..4e81181  main -> main ✅
🔹 ÉTAPE 1 — Mettre à jour PASSATION.md
Ouvre C:\Dev\rf-engineering-2-0\PASSATION.md dans VS Code.

Va à la toute fin du fichier et ajoute ceci :

markdown
---

## 24. Mise à jour du 3 octobre 2026 — RF Analytics : Bulletins PDF

### Statut : Killer feature opérationnelle ✅

### A. Nouveaux services

| Fichier | Rôle |
|---|---|
| `backend/app/services/analytics_service.py` | Agrégation des KPI (scores, breakdown, tendances) |
| `backend/app/services/bulletin_service.py` | Génération PDF via Jinja2 + Playwright |

### B. Nouvelles routes API

| Route | Méthode | Description |
|---|---|---|
| `/api/bulletins/generate` | POST | Génère un bulletin (retourne chemins) |
| `/api/bulletins/` | GET | Liste les bulletins existants |
| `/api/bulletins/download/{filename}` | GET | Télécharge un PDF |

### C. Template bulletin

- Fichier : `backend/app/templates/bulletin.html`
- ~347 lignes (HTML + CSS + Jinja2)
- Design multi-tenant (couleurs configurables par tenant)
- Sections : Score global, KPI, Tendance, Top problèmes, Top succès, Impact business

### D. Test validé

**Bulletin généré :**
- Health Score : **86/100**
- PDF : 265 Ko
- Nom : `bulletin_DigicelHaiti_20261003_165922.pdf`

### E. Corrections importantes

**1. `config.py` — `BASE_DIR` corrigé**
```python
# AVANT (mauvais) :
BASE_DIR = Path(__file__).parent.parent.parent

# APRÈS (correct) :
BASE_DIR = Path(__file__).parent.parent
Raison : config.py est dans backend/app/, donc parent.parent = backend/ (racine du projet).

2. Slugification des noms de fichiers

Problème : Digicel Haïti → accents (ï) cassaient les URLs

Solution : unicodedata.normalize("NFKD", ...) pour retirer les accents

Résultat : bulletin_DigicelHaiti_...pdf (sans tréma)

F. Docker — Accès aux fichiers générés
Volume monté : ./backend:/app → les PDFs sont directement accessibles sur le PC dans C:\Dev\rf-analytics\backend\bulletins\

Plus besoin de docker cp (qui bug sur Windows avec certains noms)

G. Commandes de test
powershell
# Générer un bulletin (via Swagger)
POST /api/bulletins/generate?hours=168

# Le PDF apparaît dans :
C:\Dev\rf-analytics\backend\bulletins\bulletin_*.pdf

# Ou télécharger via API :
GET /api/bulletins/download/bulletin_*.pdf
H. Prochaine session
Options :

🎨 Frontend RF Analytics (page login + dashboard)

🚨 Service d'alertes (détection anomalies)

📅 Scheduler (génération auto hebdo + envoi email)

💳 Stripe Billing

🚀 Déploiement (Cloudflare Tunnel + Render)

text

**Sauvegarde (Ctrl+S).**

---

## 🔹 ÉTAPE 2 — Commit + push

Dans PowerShell :

```powershell
cd C:\Dev\rf-engineering-2-0
git add PASSATION.md
git commit -m "PASSATION: section 24 - bulletins PDF opérationnels"
git push
📋 Récapitulatif
#	Action	Statut
✅	Commit rf-analytics	Fait
⏳	Éditer PASSATION.md	À faire
⏳	Commit rf-engineering-2-0	À faire
Fais l'Étape 1 (éditer) + Étape 2 (commit/push) et dis-moi quand c'est fait. 🚀

Ensuite on pourra faire le bilan de la session. 🎯

---

## 25. Mise à jour du 3 octobre 2026 — RF Analytics : Frontend + Alertes + Scheduler + Stripe + Déploiement

### Statut : RF Analytics EN LIGNE via Cloudflare Tunnel ✅

### URL publique (temporaire)

https://ordinary-corporations-russell-looksmart.trycloudflare.com

⚠️ URL change à chaque redémarrage de `cloudflared`. Pour URL fixe → acheter un domaine.

### Fonctionnalités ajoutées

**Frontend complet :**
- `frontend/login.html` — page de connexion
- `frontend/index.html` — dashboard (KPI + alertes)
- `frontend/billing.html` — page d'abonnement Stripe
- `frontend/css/style.css` — design cohérent
- `frontend/js/auth.js` — helpers JWT

**Service d'alertes :**
- Détection automatique : DCR, DL, RRC SR, PRB, Health
- Seuils : critical / high / medium
- 4 endpoints : `/scan`, `/`, `/{id}/acknowledge`, `/{id}/resolve`

**Scheduler automatique :**
- Scan alertes : toutes les heures
- Bulletins : lundi 8h UTC
- Container dédié : `rf-analytics-scheduler`

**Stripe Billing :**
- `stripe_service.py` + `billing.py`
- 3 endpoints : `/plans`, `/checkout`, `/webhook`
- 2 plans : Starter (390$), Pro (1490$)

### Docker Compose (4 services)

| Service | Rôle |
|---|---|
| `db` | PostgreSQL + TimescaleDB |
| `backend` | FastAPI + uvicorn |
| `worker` | Ingestion KPI (5 min) |
| `scheduler` | Alertes + bulletins auto |

### Commandes

```powershell
# Démarrer
cd C:\Dev\rf-analytics
docker compose up -d

# Tunnel Cloudflare
cloudflared tunnel --url http://localhost:8001


