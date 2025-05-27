interface ProgressBarProps {
  value1: number
  value2: number
}

export default function ProgressBar({ value1, value2 }: ProgressBarProps) {
  return (
    <div className="flex h-6 w-full overflow-hidden rounded">
      <div className="bg-[#00437a] h-full" style={{ width: `${value1}%` }}></div>
      <div className="bg-[#4cc7f4] h-full" style={{ width: `${value2}%` }}></div>
    </div>
  )
}

