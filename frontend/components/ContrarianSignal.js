export default function ContrarianSignal({ prediction, publicBets }) {
  const homeSignal = prediction.win_probability.home - publicBets.home;
  const awaySignal = prediction.win_probability.away - publicBets.away;
  return (
    <div className="border p-2 mb-2">
      <h2 className="font-bold">Contrarian Signal</h2>
      <p>{homeSignal > awaySignal ? "Bet Home" : "Bet Away"}</p>
    </div>
  );
}
