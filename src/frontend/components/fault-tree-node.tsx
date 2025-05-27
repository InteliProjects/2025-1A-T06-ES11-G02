import ProgressBar from "./progress-bar"
import { ChevronRight } from "lucide-react"

interface Fault {
  id: number
  name: string
  value1: number
  value2: number
}

interface Subcategory {
  id: number
  name: string
  faults: Fault[]
}

interface FaultTreeNodeProps {
  name: string
  subcategories: Subcategory[]
}

export default function FaultTreeNode({ name, subcategories }: FaultTreeNodeProps) {
  return (
    <div className="space-y-6">
      <div className="bg-[#00437a] text-white p-3 rounded-md font-medium">{name}</div>

      {subcategories.map((subcategory) => (
        <div key={subcategory.id} className="space-y-4">
          <div className="flex items-center">
            <ChevronRight className="h-4 w-4 text-[#00437a]" />
            <div className="ml-2 font-medium text-[#00437a]">{subcategory.name}</div>
          </div>

          <div className="pl-6 space-y-4">
            {subcategory.faults.map((fault) => (
              <div key={fault.id} className="space-y-1">
                <div className="text-xs text-[#5f6d7e]">{fault.name}</div>
                <ProgressBar value1={fault.value1} value2={fault.value2} />
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  )
}

