export default function PredictionPanel({ prediction }) {
  return (
    <div className="border p-2 mb-2">
      <h2 className="font-bold">Prediction</h2>
      <p>Home Score: {prediction.predicted_score.home}</p>
      <p>Away Score: {prediction.predicted_score.away}</p>
      <p>Home Win %: {prediction.win_probability.home * 100}%</p>
      <p>Away Win %: {prediction.win_probability.away * 100}%</p>
    </div>
  );
}
