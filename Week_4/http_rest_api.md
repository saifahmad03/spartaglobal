# HTTP & REST API Notes

## Contents
1. [HTTP basics](#1-http-basics)
2. [Stateless applications](#2-stateless-applications)
3. [HTTP request methods](#3-http-request-methods)
4. [HTTP status codes](#4-http-status-codes)
5. [REST API](#5-rest-api)
6. [REST constraints](#6-rest-constraints)
7. [REST benefits](#7-rest-benefits)
8. [Quick cheat sheet](#8-quick-cheat-sheet)

---

## 1. HTTP basics

- **HTTP** (HyperText Transfer Protocol): application-layer, request-response protocol. Runs over TCP (HTTP/1.1, HTTP/2) or QUIC (HTTP/3). HTTPS = HTTP + TLS encryption.
- **Client** sends a request, **server** sends back a response.

**Request structure**
```
METHOD /path?query=1 HTTP/1.1      <- request line
Host: api.example.com              <- headers
Authorization: Bearer <token>
Content-Type: application/json

{ "name": "Ada" }                  <- body (optional)
```

**Response structure**
```
HTTP/1.1 201 Created               <- status line
Content-Type: application/json
Location: /users/42                <- headers

{ "id": 42, "name": "Ada" }        <- body
```

**Common headers**

| Header | Purpose |
|---|---|
| `Content-Type` | Format of the body being sent (`application/json`) |
| `Accept` | Format the client wants back |
| `Authorization` | Credentials (Bearer token, Basic) |
| `Cache-Control` / `ETag` | Caching and conditional requests |
| `Location` | URL of a newly created resource / redirect target |
| `User-Agent` | Identifies the client |

---

## 2. Stateless applications

**Definition:** the server stores **no client session state** between requests. Every request must carry **all the information** needed to understand and process it.

- HTTP itself is stateless: each request is independent, and the server does not remember previous ones.
- Any "state" (login, cart) is added on top via cookies, sessions or tokens.

**Stateless vs stateful**

| | Stateless | Stateful |
|---|---|---|
| Server remembers client? | No | Yes (session store) |
| Each request | Self-contained | Depends on earlier requests |
| Scaling | Easy: any server can handle any request | Harder: sticky sessions or shared session store |
| Example | REST API with JWT | Traditional server-side session login |

**How state is handled in a stateless design**
- Client sends credentials every request (e.g. `Authorization: Bearer <JWT>`).
- Session data lives on the **client** (token, local storage) or in a **shared external store** (DB, Redis), not in the app server's memory.
- Resource state (DB records) is still stored. Only **session/conversation state** is not.

**Benefits**
- Horizontal scaling and easy load balancing (no sticky sessions)
- Reliability: a server can crash or be replaced without losing sessions
- Simpler server logic and easier caching
- Requests can be understood in isolation (easier debugging and monitoring)

**Drawbacks**
- Larger requests (repeated auth data or context on every call)
- Extra processing per request (e.g. validating a token every time)
- Client has to manage its own state

---

## 3. HTTP request methods

| Method | Purpose | Has body? | Safe | Idempotent |
|---|---|---|---|---|
| **GET** | Retrieve a resource | No | Yes | Yes |
| **POST** | Create a resource / trigger an action | Yes | No | No |
| **PUT** | Replace a resource entirely (or create at a known URL) | Yes | No | Yes |
| **PATCH** | Partially update a resource | Yes | No | Not guaranteed |
| **DELETE** | Remove a resource | Optional | No | Yes |
| **HEAD** | Same as GET but headers only (no body) | No | Yes | Yes |
| **OPTIONS** | Ask which methods/features the server supports (CORS preflight) | No | Yes | Yes |
| **CONNECT** | Open a tunnel (e.g. via proxy for HTTPS) | n/a | No | No |
| **TRACE** | Loop back the request for diagnostics (usually disabled) | No | Yes | Yes |

**Key terms**
- **Safe:** does not change server state (read-only).
- **Idempotent:** making the same request many times has the **same effect** as making it once (the response may differ).

**PUT vs PATCH vs POST**
- `PUT /users/42` sends the **full** representation and replaces the resource.
- `PATCH /users/42` sends **only changed fields**.
- `POST /users` creates a new resource, and the server picks the ID. Repeating it creates duplicates.

**CRUD mapping**

| CRUD | HTTP | Example |
|---|---|---|
| Create | POST | `POST /users` |
| Read | GET | `GET /users`, `GET /users/42` |
| Update | PUT / PATCH | `PUT /users/42` |
| Delete | DELETE | `DELETE /users/42` |

---

## 4. HTTP status codes

**Classes**

| Range | Meaning |
|---|---|
| **1xx** | Informational |
| **2xx** | Success |
| **3xx** | Redirection |
| **4xx** | Client error (your request is wrong) |
| **5xx** | Server error (server failed) |

### 1xx Informational
| Code | Name | Notes |
|---|---|---|
| 100 | Continue | Client may continue sending the body |
| 101 | Switching Protocols | e.g. upgrade to WebSocket |

### 2xx Success
| Code | Name | When to use |
|---|---|---|
| **200** | OK | Standard success (GET, PUT, PATCH) |
| **201** | Created | Resource created (POST); include `Location` header |
| **202** | Accepted | Request accepted, processed asynchronously |
| **204** | No Content | Success, no body (typical for DELETE / PUT) |

### 3xx Redirection
| Code | Name | Notes |
|---|---|---|
| **301** | Moved Permanently | URL changed forever (cached, SEO) |
| **302** | Found | Temporary redirect |
| **304** | Not Modified | Cached copy is still valid (conditional GET) |
| **307** | Temporary Redirect | Temporary, **method preserved** |
| **308** | Permanent Redirect | Permanent, **method preserved** |

### 4xx Client errors
| Code | Name | When to use |
|---|---|---|
| **400** | Bad Request | Malformed syntax / invalid request |
| **401** | Unauthorized | Not authenticated (missing/invalid credentials) |
| **403** | Forbidden | Authenticated but **not allowed** |
| **404** | Not Found | Resource doesn't exist |
| **405** | Method Not Allowed | Method not supported on this resource |
| **406** | Not Acceptable | Can't produce the format in `Accept` |
| **408** | Request Timeout | Client took too long |
| **409** | Conflict | State conflict (duplicate, edit conflict) |
| **410** | Gone | Resource permanently removed |
| **415** | Unsupported Media Type | Bad `Content-Type` |
| **422** | Unprocessable Content | Well-formed, but fails validation |
| **429** | Too Many Requests | Rate limit hit |

### 5xx Server errors
| Code | Name | When to use |
|---|---|---|
| **500** | Internal Server Error | Generic unexpected server failure |
| **501** | Not Implemented | Server doesn't support the feature/method |
| **502** | Bad Gateway | Invalid response from upstream server |
| **503** | Service Unavailable | Overloaded / down for maintenance |
| **504** | Gateway Timeout | Upstream server timed out |

**Memory tips**
- **401** = "who are you?" (authentication). **403** = "I know you, but no" (authorization).
- **400** = malformed request. **422** = well-formed but semantically invalid.
- **404** = missing. **410** = deliberately gone.
- **4xx** = fix the request. **5xx** = server's problem (retrying may help).

---

## 5. REST API

- **REST** = **RE**presentational **S**tate **T**ransfer, an **architectural style** (Roy Fielding, 2000), not a protocol or standard.
- A **RESTful API** exposes **resources** over HTTP using standard methods and URLs.
- **Resource:** any "thing" (user, order, product), identified by a **URI**.
- **Representation:** the format a resource is transferred in, usually **JSON** (also XML, HTML).

**URL design conventions**
- Use **nouns**, not verbs: `/users`, not `/getUsers`
- Plural collections: `/users`, `/users/42`
- Nest for relationships: `/users/42/orders`
- Use query params for filter/sort/paginate: `/users?role=admin&sort=name&page=2`
- Version the API: `/v1/users`
- Lowercase, hyphen-separated: `/order-items`

**Example**
```
GET    /v1/users          -> list users
GET    /v1/users/42       -> get one user
POST   /v1/users          -> create user        (201 + Location)
PUT    /v1/users/42       -> replace user       (200/204)
PATCH  /v1/users/42       -> update fields      (200/204)
DELETE /v1/users/42       -> delete user        (204)
```

---

## 6. REST constraints

The 6 architectural constraints (an API must follow the first five to be truly RESTful; the last is optional).

### 1. Client-Server
- Client (UI) and server (data/logic) are **separated** and evolve independently.
- Enables portability (one API, many clients) and scalability.

### 2. Stateless
- Each request contains **everything** the server needs. No stored client context on the server.
- See [section 2](#2-stateless-applications).

### 3. Cacheable
- Responses must label themselves **cacheable or not** (`Cache-Control`, `ETag`, `Expires`).
- Reduces load and latency and improves performance.

### 4. Uniform Interface
The core constraint. A consistent, standard way to interact. It has 4 sub-constraints:
1. **Resource identification:** resources identified by URIs.
2. **Manipulation through representations:** clients change resources via representations (e.g. JSON) they send and receive.
3. **Self-descriptive messages:** each message says how to process it (`Content-Type`, method, status codes).
4. **HATEOAS** (Hypermedia As The Engine Of Application State): responses include **links** to related actions/resources so clients can navigate dynamically.

### 5. Layered System
- Client can't tell if it's connected directly to the end server or an intermediary (load balancer, proxy, gateway, CDN).
- Allows security layers, load balancing and caching.

### 6. Code on Demand *(optional)*
- Server can send **executable code** to the client (e.g. JavaScript) to extend functionality.

**Quick recall:** **C**lient-server, **S**tateless, **C**acheable, **U**niform interface, **L**ayered, **C**ode on demand (optional).

---

## 7. REST benefits

| Benefit | Why |
|---|---|
| **Scalability** | Stateless servers + caching make horizontal scaling easy |
| **Simplicity** | Uses plain HTTP, URLs and standard methods, so it is easy to learn and debug |
| **Flexibility** | Supports multiple formats (JSON, XML) and any client (web, mobile, IoT) |
| **Independence** | Client and server evolve separately (as long as the interface is stable) |
| **Performance** | Built-in HTTP caching reduces server load and latency |
| **Portability** | Language- and platform-agnostic |
| **Visibility / reliability** | Self-contained requests are easy to monitor, log and retry |
| **Wide ecosystem** | Huge tooling support (Postman, OpenAPI/Swagger, curl) |

**Common drawbacks / trade-offs**
- **Over-fetching / under-fetching:** fixed endpoints may return too much or too little data (GraphQL addresses this).
- **Multiple round trips** to assemble related data.
- **No built-in standard** for things like auth, pagination, or error format. Teams must agree on conventions.
- **Stateless overhead:** repeated auth/context data on every request.
- **Not ideal** for real-time/streaming (WebSockets, SSE, gRPC fit better).

---

## 8. Quick cheat sheet

- **HTTP** is stateless. **REST** builds on HTTP with 6 constraints.
- **Safe methods:** GET, HEAD, OPTIONS. **Idempotent:** GET, PUT, DELETE, HEAD, OPTIONS. **Not idempotent:** POST (PATCH not guaranteed).
- **Status code ranges:** 1xx info, 2xx success, 3xx redirect, 4xx client error, 5xx server error.
- **Most-used codes:** 200, 201, 204, 301, 304, 400, 401, 403, 404, 409, 422, 429, 500, 503.
- **URL rules:** nouns, plural, nested for relationships, versioned.
- **Core REST ideas:** resources + URIs + standard HTTP verbs + stateless requests + representations (JSON).