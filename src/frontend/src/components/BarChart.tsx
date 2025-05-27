"use client"

import { useEffect, useRef } from "react"
import { Chart, registerables } from "chart.js"

Chart.register(...registerables)

export default function BarChart() {
  const chartRef = useRef<HTMLCanvasElement>(null)
  const chartInstance = useRef<Chart | null>(null)

  useEffect(() => {
    if (chartRef.current) {
      const ctx = chartRef.current.getContext("2d")

      if (ctx) {
        if (chartInstance.current) {
          chartInstance.current.destroy()
        }

        chartInstance.current = new Chart(ctx, {
          type: "bar",
          data: {
            labels: [
              "Problema na bateria",
              "Desgaste do tempo",
              "Manutenção de",
              "Sistema elétrico",
              "Falha no ar-condicionado",
              "Caixa manual de marchas",
              "Chicote de fiação",
              "Circuito de freio",
              "Circuito hidráulico",
              "Falha no ar-condicionado",
            ],
            datasets: [
              {
                data: [1000, 900, 700, 650, 600, 550, 500, 400, 300, 200],
                backgroundColor: "#00437a",
                barPercentage: 0.8,
                categoryPercentage: 0.7,
              },
            ],
          },
          options: {
            indexAxis: "y",
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              x: {
                beginAtZero: true,
                grid: {
                  color: "#e6e9ec",
                },
                ticks: {
                  callback: (value) => {
                    if (typeof value === "number") {
                      return value === 0 ? "0" : value === 500 ? "500" : value === 1000 ? "1000" : ""
                    }
                    return value
                  },
                },
              },
              y: {
                grid: {
                  display: false,
                },
              },
            },
            plugins: {
              legend: {
                display: false,
              },
            },
          },
        })
      }
    }

    return () => {
      if (chartInstance.current) {
        chartInstance.current.destroy()
      }
    }
  }, [])

  return (
    <div style={{ height: "400px" }}>
      <canvas ref={chartRef}></canvas>
    </div>
  )
}

