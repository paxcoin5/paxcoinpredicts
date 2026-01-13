export default function PublicBetsPanel({ publicBets }) {
  return (
    <div className="border p-2 mb-2">
      <h2 className="font-bold">Public Bets</h2>
      <p>Home: {publicBets.home * 100}%</p>
      <p>Away: {publicBets.away * 100}%</p>
    </div>
  );
}
