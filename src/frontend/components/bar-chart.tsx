"use client"

import { useEffect, useRef } from "react"
import { Chart, registerables } from "chart.js"

Chart.register(...registerables)

export default function BarChart() {
  const chartRef = useRef<HTMLCanvasElement>(null)
  const chartInstance = useRef<Chart | null>(null)

  useEffect(() => {
    async function fetchData() {
      const res = await fetch("https://api-m11.fly.dev/dados/falhas/falhas-por-tipo")
      const json = await res.json()

      const nomeFalhas: Record<number, string> = {
        126: "Problema na bateria",
        123: "Desgaste do tempo",
        125: "Sistema elétrico",
        68: "Falha no ar-condicionado",
        30: "Caixa manual de marchas",
        9793885: "Chicote de fiação",
        109: "Circuito de freio",
        107: "Circuito hidráulico",
        141: "Painel de controle",
        100: "Sensor de velocidade",
        73: "Falha no motor",
        98721257: "Conexão de rede",
        81: "Sistema de injeção",
      }

      const labels = json.data.map((item: [number, number]) => nomeFalhas[item[0]] || `Código ${item[0]}`)
      const values = json.data.map((item: [number, number]) => item[1])

      if (chartRef.current) {
        const ctx = chartRef.current.getContext("2d")

        if (ctx) {
          if (chartInstance.current) {
            chartInstance.current.destroy()
          }

          chartInstance.current = new Chart(ctx, {
            type: "bar",
            data: {
              labels,
              datasets: [
                {
                  data: values,
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
                        return value === 0 ? "0" : value === 1 ? "1" : value === 2 ? "2" : ""
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
    }

    fetchData()

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
