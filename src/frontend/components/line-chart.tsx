"use client"

import { useEffect, useRef } from "react"
import { Chart, registerables } from "chart.js"

Chart.register(...registerables)

export default function LineChart() {
  const chartRef = useRef<HTMLCanvasElement>(null)
  const chartInstance = useRef<Chart | null>(null)

  useEffect(() => {
    async function fetchData() {
      const res = await fetch("https://api-m11.fly.dev/dados/falhas/falhas-diarias")
      const json = await res.json()

      const labels = json.data.map((item: [string, number]) => item[0])
      const values = json.data.map((item: [string, number]) => item[1])
      const mediaValue = json.media[0][0]
      const media = new Array(labels.length).fill(mediaValue)

      if (chartRef.current) {
        const ctx = chartRef.current.getContext("2d")

        if (ctx) {
          if (chartInstance.current) {
            chartInstance.current.destroy()
          }

          chartInstance.current = new Chart(ctx, {
            type: "line",
            data: {
              labels,
              datasets: [
                {
                  label: "Falhas",
                  data: values,
                  borderColor: "#00437a",
                  backgroundColor: "transparent",
                  tension: 0.1,
                },
                {
                  label: "Média",
                  data: media,
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
    }

    fetchData()

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
