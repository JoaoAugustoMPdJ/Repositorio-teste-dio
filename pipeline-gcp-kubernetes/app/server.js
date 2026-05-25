const express = require("express");

const app = express();
const port = process.env.PORT || 8080;

app.get("/", (req, res) => {
  res.json({
    mensagem: "Deploy realizado com sucesso no Kubernetes GKE!",
    projeto: "Pipeline CI/CD com Docker, Cloud Build e GCP",
    status: "online"
  });
});

app.get("/health", (req, res) => {
  res.status(200).json({
    status: "healthy"
  });
});

app.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});