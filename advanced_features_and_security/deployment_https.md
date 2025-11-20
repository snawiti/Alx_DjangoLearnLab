# HTTPS Deployment Configuration

This project enforces HTTPS and secure redirects using the following Django settings:

- `SECURE_SSL_REDIRECT=True`: Forces all HTTP requests to redirect to HTTPS.
- `SECURE_HSTS_SECONDS=31536000`: Enables HTTP Strict Transport Security (HSTS).
- `SECURE_HSTS_INCLUDE_SUBDOMAINS=True`: Applies HSTS to all subdomains.
- `SECURE_HSTS_PRELOAD=True`: Enables support for browser preloading.
- `SESSION_COOKIE_SECURE=True` and `CSRF_COOKIE_SECURE=True`: Ensures cookies are only sent over HTTPS.
- `X_FRAME_OPTIONS="DENY"`: Protects against clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF=True`: Prevents MIME-type sniffing.
- `SECURE_BROWSER_XSS_FILTER=True`: Adds browser XSS protection.

## Web Server SSL Configuration

### Nginx Example

