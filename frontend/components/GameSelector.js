export default function GameSelector({ games, selectedGame, setSelectedGame }) {
  return (
    <div className="mb-4">
      <label className="mr-2">Game:</label>
      <select value={selectedGame} onChange={e => setSelectedGame(e.target.value)}>
        <option value="">Select a game</option>
        {Object.keys(games).map(id => (
          <option key={id} value={id}>
            {games[id].away_team} @ {games[id].home_team}
          </option>
        ))}
      </select>
    </div>
  );
}
