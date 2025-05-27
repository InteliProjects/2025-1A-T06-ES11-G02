"use client"

import { useEffect, useState } from "react"
import { format, subDays, parseISO } from "date-fns"
import { Sidebar } from "@/components/sidebar"
import { AlertCircle } from "lucide-react"
import LineChart from "@/components/line-chart"
import BarChart from "@/components/bar-chart"

export default function DashboardPage() {
  const [modelosAfetados, setModelosAfetados] = useState<{ modelo: string, qtd: number }[]>([])
  const [veiculos24h, setVeiculos24h] = useState<number | null>(null)

  useEffect(() => {
    async function fetchModelos() {
      const res = await fetch("https://api-m11.fly.dev/dados/falhas/erros-por-modelo")
      const json = await res.json()
      const dados = json.data.map((item: [string, number]) => ({
        modelo: item[0].trim(),
        qtd: item[1]
      }))
      setModelosAfetados(dados)
    }

    async function fetchVeiculos() {
      const res = await fetch("https://api-m11.fly.dev/dados/falhas/carros-afetados-por-dia")
      const json = await res.json()
      const ontem = format(subDays(new Date(), 1), "yyyy-MM-dd")
      const item = json.data.find((item: [string, number]) => item[0] === ontem)
      setVeiculos24h(item ? item[1] : 0)
    }

    fetchModelos()
    fetchVeiculos()
  }, [])

  return (
    <div className="flex h-screen bg-[#f9fbfd]">
      <Sidebar />
      <div className="flex-1 p-6 overflow-auto">
        
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-2xl font-semibold">Acompanhamento - Geral</h1>
          <div className="text-sm text-[#5f6d7e]">
  Data da consulta: {format(new Date(), "dd/MM/yyyy")}
</div>
        </div>

        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
          
          <div className="p-6 text-center bg-white rounded-lg border-2 border-red-500 shadow-sm">
            <div className="text-5xl font-bold">{veiculos24h !== null ? veiculos24h : "-"}</div>
            <div className="mt-2 text-sm text-[#5f6d7e]">
              Veículos com falhas<br />nas últimas 24 horas
            </div>
          </div>
        
          
          <div className="p-4 bg-white rounded-lg border shadow-sm">
            <h3 className="text-sm font-medium mb-3">Modelos mais afetados</h3>
            <div className="space-y-2">
              {modelosAfetados.map(({ modelo, qtd }) => {
                const max = modelosAfetados[0]?.qtd || 1
                const percent = Math.round((qtd / max) * 100)
                return (
                  <div key={modelo} className="flex items-center justify-between">
                    <span className="text-xs">{modelo}</span>
                    <div className="w-24 h-2 bg-gray-100 rounded-full overflow-hidden">
                      <div className="h-full bg-[#00437a]" style={{ width: `${percent}%` }}></div>
                    </div>
                  </div>
                )
              })}
            </div>
          </div>
        </div>
        
        <div className="grid grid-cols-1 gap-6">
          <div className="p-4 bg-white rounded-lg border shadow-sm">
            <h2 className="text-lg font-medium mb-2">Evolução das Falhas</h2>
            <p className="text-sm text-[#5f6d7e] mb-4">Este gráfico mostra a evolução do número de veículos com falhas ao longo do tempo.</p>
            <LineChart />
          </div>
          <div className="p-6 bg-white rounded-lg border shadow-sm">
            <h2 className="text-lg font-medium mb-4">Principais problemas</h2>
            <p className="text-sm text-[#5f6d7e] mb-4">Este gráfico exibe os principais problemas identificados no período analisado.</p>
            <BarChart />
          </div>
        </div>
      </div>
    </div>
  )
}
