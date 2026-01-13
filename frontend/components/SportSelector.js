export default function SportSelector({ sport, setSport }) {
  return (
    <div className="mb-2">
      <label className="mr-2">Sport:</label>
      <select value={sport} onChange={e => setSport(e.target.value)}>
        <option value="NFL">NFL</option>
        <option value="NBA">NBA</option>
        <option value="NCAAB">NCAAB</option>
      </select>
    </div>
  );
}
