import Link from "next/link"

export function Sidebar() {
  return (
    <div className="w-64 bg-[#dfe4e8] h-full flex flex-col">
      <div className="p-4 flex items-center space-x-3">
        <div className="w-8 h-8 rounded-full bg-[#7c8b9d] flex items-center justify-center">
          <span className="text-white text-xs">UT</span>
        </div>
        <span className="text-sm font-medium text-[#5f6d7e]">Usuário Teste</span>
        <div className="h-1 bg-[#d9d9d9] flex-1"></div>
      </div>

      <div className="mt-8 px-4 space-y-2">
        <Link href="/dashboard" className="block py-2 px-4 rounded bg-[#7c8b9d] text-white text-sm font-medium">
          HOME
        </Link>
        <Link href="/data" className="block py-2 px-4 rounded bg-[#7c8b9d] text-white text-sm font-medium">
          GESTÃO DE FALHAS
        </Link>
      </div>

      <div className="mt-4 px-4">
        <div className="border-t border-[#d1d9e2]"></div>
      </div>
    </div>
  )
}

