# Security

## Reporting vulnerabilities

If you discover a security issue, please open a **private** advisory on GitHub (or contact the repository owner through your course or institutional channel). Do not post secrets, connection strings, or keys in public issues.

## Secrets in this project

- **Never commit** `.env`, raw Kubernetes `Secret` manifests with real data, or connection strings with passwords.
- Prefer [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/) or sealed secrets / external secret operators for production clusters.
- The sample manifests in `bookstore-app/YAML/` use **placeholders**. Replace them locally and keep real files out of version control if you use a different workflow.

## If credentials were exposed

If a MongoDB / Cosmos DB connection string or account key was ever committed or shared publicly:

1. **Rotate** the key in the Azure portal (Cosmos DB → Keys → Regenerate).
2. Update your local `.env` and cluster secrets only on trusted machines.
3. Consider the old key compromised even after removing it from git history.
