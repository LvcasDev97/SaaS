async function carregarCards() {
    try {
        const res = await fetch("/sales/stats");
        const data = await res.json();

        document.getElementById("card-vendas").textContent = data.vendas;
        document.getElementById("card-produtos").textContent = data.produtos;
        document.getElementById("card-usuarios").textContent = data.usuarios;
    } catch (error) {
        console.error("Erro ao carregar estatísticas:", error);
    }
}

async function carregarGrafico() {
    try {
        const res = await fetch("/sales/report");
        const data = await res.json();

        const labels = data.map(item => item.produto);
        const valores = data.map(item => item.total);

        new Chart(document.getElementById("grafico"), {
            type: "bar",
            data: {
                labels: labels,
                datasets: [{
                    label: "Quantidade Vendida",
                    data: valores,
                    backgroundColor: [
                        "rgba(75, 192, 192, 0.6)",
                        "rgba(255, 99, 132, 0.6)",
                        "rgba(255, 206, 86, 0.6)",
                        "rgba(54, 162, 235, 0.6)",
                        "rgba(153, 102, 255, 0.6)"
                    ],
                    borderColor: "rgba(0,0,0,0.1)",
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    title: {
                        display: true,
                        text: "Relatório de Vendas",
                        font: { size: 20 }
                    },
                    legend: { display: false }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        title: { display: true, text: "Quantidade" }
                    },
                    x: {
                        title: { display: true, text: "Produtos" }
                    }
                }
            }
        });
    } catch (error) {
        console.error("Erro ao carregar gráfico:", error);
    }
}

// Inicializa o dashboard
carregarCards();
carregarGrafico();

// Atualiza automaticamente a cada 30 segundos
setInterval(() => {
    carregarCards();
    carregarGrafico();
}, 30000);

