"use client"

import { useEffect, useRef } from "react"
import { Chart, registerables } from "chart.js"

Chart.register(...registerables)

export default function LineChart() {
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
          type: "line",
          data: {
            labels: [
              "Jan/22",
              "Fev/22",
              "Mar/22",
              "Abr/22",
              "Mai/22",
              "Jun/22",
              "Jul/22",
              "Ago/22",
              "Set/22",
              "Out/22",
              "Nov/22",
            ],
            datasets: [
              {
                label: "Falhas",
                data: [8000, 9000, 6500, 10000, 8500, 7000, 3500, 4000, 5500, 7000, 11000],
                borderColor: "#00437a",
                backgroundColor: "transparent",
                tension: 0.1,
              },
              {
                label: "Média",
                data: [7000, 7000, 7000, 7000, 7000, 7000, 7000, 7000, 7000, 7000, 7000],
                borderColor: "#4cc7f4",
                backgroundColor: "transparent",
                borderDash: [5, 5],
              },
            ],
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              y: {
                beginAtZero: true,
                grid: {
                  color: "#e6e9ec",
                },
              },
              x: {
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
    <div style={{ height: "300px" }}>
      <canvas ref={chartRef}></canvas>
    </div>
  )
}

