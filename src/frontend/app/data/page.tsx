"use client";
export const dynamic = "force-dynamic";

import { useState } from "react";
import { format } from "date-fns";
import { ptBR } from "date-fns/locale";
import { Sidebar } from "@/components/sidebar";
import { Calendar } from "@/components/ui/calendar";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";

export default function DataPage() {
  const [startDate, setStartDate] = useState<Date>();
  const [endDate, setEndDate] = useState<Date>();
  const [ponto, setPonto] = useState<string>("");

  const [pctData, setPctData] = useState<any[]>([]);
  const [periodData, setPeriodData] = useState<any[]>([]);
  const [statusEtapasData, setStatusEtapasData] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [viewMode, setViewMode] = useState<"tree" | "graph">("tree");

  const formatDate = (date: Date | undefined) => {
    if (!date) return "";
    return format(date, "dd/MM/yyyy", { locale: ptBR });
  };

  const handleAnalysis = async () => {
    if (!startDate || !endDate || !ponto) {
      alert("Por favor, selecione todas as opções de filtro.");
      return;
    }
    const formattedStart = format(startDate, "yyyy-MM-dd");
    const formattedEnd = format(endDate, "yyyy-MM-dd");
    setIsLoading(true);
    try {
      const res = await fetch(
        `https://api-m11.fly.dev/arvore-falhas/pct-por-tipo?data_inicio=${formattedStart}&data_fim=${formattedEnd}&ponto=${ponto}`
      );
      const json = await res.json();
      setPctData(json.data);
      setPeriodData([]);
      setStatusEtapasData(null);
    } catch (error) {
      console.error("Erro ao buscar análise:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleClickFailure = async (typeId: number) => {
    if (!startDate || !endDate || !ponto) {
      alert("Por favor, selecione todas as opções de filtro.");
      return;
    }
    const formattedStart = format(startDate, "yyyy-MM-dd");
    const formattedEnd = format(endDate, "yyyy-MM-dd");
    setIsLoading(true);
    try {
      const resTree = await fetch(
        `https://api-m11.fly.dev/arvore-falhas/falhas-por-periodo?data_inicio=${formattedStart}&data_fim=${formattedEnd}&ponto=${ponto}&type_id=${typeId}`
      );
      const jsonTree = await resTree.json();
      setPeriodData(jsonTree.data);
      const resGraph = await fetch(
        `https://api-m11.fly.dev/arvore-falhas/status-etapas?data_inicio=${formattedStart}&data_fim=${formattedEnd}&ponto=${ponto}&type_id=${typeId}`
      );
      const jsonGraph = await resGraph.json();
      setStatusEtapasData(jsonGraph.data);
      setViewMode("tree");
    } catch (error) {
      console.error("Erro ao buscar dados:", error);
    } finally {
      setIsLoading(false);
    }
  };

  const allPoints = ["AGUA", "DKA_ZP8", "PROCESSO", "RODAGEM", "ZP5", "ZP5A", "ZP6", "ZP7"];

  return (
    <div className="flex h-screen bg-[#f9fbfd]">
      <Sidebar />
      <div className="flex-1 p-4 overflow-auto">
        {isLoading && (
          <div className="fixed inset-0 bg-white bg-opacity-75 flex items-center justify-center z-50">
            <div className="text-xl font-semibold">Carregando Dados...</div>
          </div>
        )}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
          <Popover>
            <PopoverTrigger asChild>
              <div className="p-3 bg-[#e6e9ec] rounded-lg border shadow-sm cursor-pointer">
                <h2 className="text-center mb-2 font-medium text-sm">Data Início</h2>
                <div className="text-center text-xs">
                  {startDate ? formatDate(startDate) : "Selecione uma data"}
                </div>
              </div>
            </PopoverTrigger>
            <PopoverContent className="w-auto p-0" align="start">
              <Calendar mode="single" selected={startDate} onSelect={setStartDate} initialFocus />
            </PopoverContent>
          </Popover>
          <Popover>
            <PopoverTrigger asChild>
              <div className="p-3 bg-[#e6e9ec] rounded-lg border shadow-sm cursor-pointer">
                <h2 className="text-center mb-2 font-medium text-sm">Data Fim</h2>
                <div className="text-center text-xs">
                  {endDate ? formatDate(endDate) : "Selecione uma data"}
                </div>
              </div>
            </PopoverTrigger>
            <PopoverContent className="w-auto p-0" align="start">
              <Calendar mode="single" selected={endDate} onSelect={setEndDate} initialFocus />
            </PopoverContent>
          </Popover>
          <div className="p-3 bg-[#e6e9ec] rounded-lg border shadow-sm">
            <h2 className="text-center mb-2 font-medium text-sm">Ponto</h2>
            <select
              className="w-full p-1 border rounded text-sm"
              value={ponto}
              onChange={(e) => setPonto(e.target.value)}
            >
              <option value="">Selecione um Ponto</option>
              {allPoints.map((pt) => (
                <option key={pt} value={pt}>
                  {pt}
                </option>
              ))}
            </select>
          </div>
        </div>
        <div className="mt-2">
          <button
            className="px-4 py-2 bg-blue-500 text-white text-sm rounded"
            onClick={handleAnalysis}
          >
            Iniciar Análise
          </button>
        </div>
        <div className="grid grid-cols-12 gap-4 mt-4">
          <div className="col-span-12 md:col-span-3">
            <h2 className="text-md font-semibold mb-3">Falhas (pct-por-tipo)</h2>
            {pctData.length > 0 ? (
              <div className="grid grid-cols-1 gap-2">
                {pctData.map((item, index) => (
                  <div
                    key={index}
                    className="p-2 bg-white border rounded shadow-sm cursor-pointer"
                    onClick={() => handleClickFailure(item.type_id)}
                  >
                    <div className="text-sm font-medium">Tipo: {item.type_id}</div>
                    <div className="text-xs">Erros: {item.contagem_erro}</div>
                    <div className="text-xs">Pct: {(item.pct * 100).toFixed(2)}%</div>
                  </div>
                ))}
              </div>
            ) : (
              <div className="text-xs text-gray-600">
                Nenhuma falha carregada. Clique em Iniciar Análise.
              </div>
            )}
          </div>
          <div className="col-span-12 md:col-span-9">
            {(periodData.length > 0 || statusEtapasData) && (
              <div className="flex items-center justify-end mb-3 space-x-2">
                <button
                  onClick={() => setViewMode("tree")}
                  className={`px-3 py-1 text-xs rounded ${
                    viewMode === "tree" ? "bg-blue-500 text-white" : "bg-gray-200 text-gray-700"
                  }`}
                >
                  Ver Árvore
                </button>
                <button
                  onClick={() => setViewMode("graph")}
                  className={`px-3 py-1 text-xs rounded ${
                    viewMode === "graph" ? "bg-blue-500 text-white" : "bg-gray-200 text-gray-700"
                  }`}
                >
                  Ver Gráfico
                </button>
              </div>
            )}
            {viewMode === "tree" ? (
              periodData.length > 0 ? (
                <div>
                  <h2 className="text-md font-semibold mb-3">Árvore de Falhas</h2>
                  {Object.entries(
                    periodData.reduce((acc, curr) => {
                      const key = curr.ponto;
                      if (!acc[key]) {
                        acc[key] = [];
                      }
                      acc[key].push(curr);
                      return acc;
                    }, {} as { [key: string]: any[] })
                  ).map(([ponto, items]) => (
                    <div key={ponto} className="mb-4">
                      <h3 className="text-sm font-semibold mb-2">{ponto}</h3>
                      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2">
                        {(items as any[]).map((item, index) => {
                          const total = item.contagem_total || 0;
                          const morningPct = total ? (item.contagem_periodo1 / total) * 100 : 0;
                          const afternoonPct = total ? (item.contagem_periodo2 / total) * 100 : 0;
                          return (
                            <div key={index} className="p-2 bg-white border rounded shadow-sm">
                              <div className="text-xs font-medium">Tipo: {item.type_id}</div>
                              <div className="text-[10px]">Manhã: {item.contagem_periodo1}</div>
                              <div className="text-[10px]">Tarde: {item.contagem_periodo2}</div>
                              <div className="text-[10px]">Total: {item.contagem_total}</div>
                              <div className="flex items-center justify-center mt-2">
                                <div
                                  className="w-8 h-8 rounded-full relative"
                                  style={{
                                    background: `conic-gradient(#3b82f6 ${(item.pct * 100).toFixed(0)}%, #d1d5db ${(item.pct * 100).toFixed(0)}% 100%)`,
                                  }}
                                >
                                  <span className="absolute inset-0 flex items-center justify-center text-[10px] font-semibold">
                                    {(item.pct * 100).toFixed(0)}%
                                  </span>
                                </div>
                              </div>
                              <div className="relative w-full h-2 bg-gray-200 rounded mt-2 overflow-hidden">
                                <div
                                  className="absolute left-0 top-0 h-2 bg-blue-400"
                                  style={{ width: `${morningPct}%` }}
                                />
                                <div
                                  className="absolute left-0 top-0 h-2 bg-green-400"
                                  style={{
                                    width: `${afternoonPct}%`,
                                    marginLeft: `${morningPct}%`,
                                  }}
                                />
                              </div>
                              <div className="mt-1 flex justify-between">
                                <div className="flex items-center">
                                  <span className="w-3 h-3 bg-blue-400 inline-block mr-1"></span>
                                  <span className="text-[10px]">Manhã</span>
                                </div>
                                <div className="flex items-center">
                                  <span className="w-3 h-3 bg-green-400 inline-block mr-1"></span>
                                  <span className="text-[10px]">Tarde</span>
                                </div>
                              </div>
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div>
                  <h2 className="text-md font-semibold mb-3">Pontos</h2>
                  <div className="grid grid-cols-4 gap-4">
                    {allPoints.map((p, idx) => (
                      <div key={idx} className="p-2 bg-white border rounded shadow-sm text-center text-sm">
                        {p}
                      </div>
                    ))}
                  </div>
                </div>
              )
            ) : viewMode === "graph" && statusEtapasData ? (
              <div>
                <h2 className="text-md font-semibold mb-3">Gráfico de Status por Etapas</h2>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  {Object.entries(statusEtapasData).map(([key, data]: [string, any]) => {
                    const t1 = data.turno1 || 0;
                    const t2 = data.turno2 || 0;
                    const t3 = data.turno3 || 0;
                    const t4 = data.troca || 0;
                    const total = t1 + t2 + t3 + t4;
                    const pct1 = total ? (t1 / total) * 100 : 0;
                    const pct2 = total ? (t2 / total) * 100 : 0;
                    const pct3 = total ? (t3 / total) * 100 : 0;
                    const pct4 = total ? (t4 / total) * 100 : 0;
                    return (
                      <div key={key} className="p-3 bg-white border rounded shadow-sm">
                        <h3 className="text-sm font-medium capitalize">{key}</h3>
                        <div className="relative w-full h-3 bg-gray-200 rounded mt-2 overflow-hidden">
                          <div
                            className="absolute left-0 top-0 h-3 bg-blue-400"
                            style={{ width: `${pct1}%` }}
                          ></div>
                          <div
                            className="absolute left-0 top-0 h-3 bg-green-400"
                            style={{ width: `${pct2}%`, marginLeft: `${pct1}%` }}
                          ></div>
                          <div
                            className="absolute left-0 top-0 h-3 bg-yellow-400"
                            style={{ width: `${pct3}%`, marginLeft: `${pct1 + pct2}%` }}
                          ></div>
                          <div
                            className="absolute left-0 top-0 h-3 bg-red-400"
                            style={{ width: `${pct4}%`, marginLeft: `${pct1 + pct2 + pct3}%` }}
                          ></div>
                        </div>
                        <div className="mt-1 flex flex-wrap gap-2 text-[10px]">
                          <div className="flex items-center">
                            <span className="w-3 h-3 bg-blue-400 inline-block mr-1"></span>
                            <span>Turno1: {t1}</span>
                          </div>
                          <div className="flex items-center">
                            <span className="w-3 h-3 bg-green-400 inline-block mr-1"></span>
                            <span>Turno2: {t2}</span>
                          </div>
                          <div className="flex items-center">
                            <span className="w-3 h-3 bg-yellow-400 inline-block mr-1"></span>
                            <span>Turno3: {t3}</span>
                          </div>
                          <div className="flex items-center">
                            <span className="w-3 h-3 bg-red-400 inline-block mr-1"></span>
                            <span>Troca: {t4}</span>
                          </div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            ) : (
              <div className="text-xs text-gray-600">Nenhum gráfico disponível.</div>
            )}
          </div>
        </div>
        <details className="mt-4 p-3 bg-white border rounded shadow-sm">
          <summary className="cursor-pointer text-sm text-gray-700 font-medium">
            Ver explicação detalhada
          </summary>
          <p className="mt-2 text-xs text-gray-700">
            Esta tela exibe, à esquerda, a lista de falhas retornadas pela rota de pct-por-tipo.
            Ao clicar em uma falha, são carregados os dados detalhados (árvore de falhas) e os dados para o gráfico
            de status por etapas (considerando Turno1, Turno2, Turno3 e Troca). Na coluna da direita, o usuário pode
            alternar entre a visualização em árvore e a visualização em gráfico.
          </p>
        </details>
      </div>
    </div>
  );
}