interface ProgressBarProps {
  value1: number
  value2: number
  correlation?: number
}

export default function ProgressBar({ value1, value2, correlation }: ProgressBarProps) {
  const primaryWidth = correlation !== undefined ? correlation * 100 : value1;
  const secondaryWidth = correlation !== undefined ? (1 - correlation) * 100 : value2;

  return (
    <div className="flex h-5 w-full overflow-hidden rounded">
      <div className="bg-[#00437a] h-full" style={{ width: `${primaryWidth}%` }}></div>
      <div className="bg-[#aec2ca] h-full" style={{ width: `${secondaryWidth}%` }}></div>
    </div>
  );
}