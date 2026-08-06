import { useState } from 'react'
import axios from 'axios'

export default function LeadForm() {
  const [form, setForm] = useState({
    name: '', email: '', company: '', budget: 10000, requirements: ''
  })
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)

 const handleSubmit = async () => {
    setLoading(true)
    try {
      const res = await axios.post('http://localhost:8000/analyze-lead', {
        ...form,
        budget: parseFloat(form.budget)
      })
      setResult(res.data)
      // Make.com webhook trigger
 axios.post('https://hook.eu1.make.com/gfdkj6vzhksxyfa8ef4elax07fyilvg7', {
  name: form.name,
  email: form.email,
  company: form.company,
  budget: form.budget,
  requirements: form.requirements,
  lead_score: res.data.lead_score,
  ai_email: res.data.ai_email
})
      // Save to localStorage
      const existing = JSON.parse(localStorage.getItem('leads') || '[]')
      localStorage.setItem('leads', JSON.stringify([...existing, res.data]))
    } catch (err) {
      alert('Error! FastAPI running hai?')
    }
    setLoading(false)
  }

  const scoreColor = {
    Hot: 'text-red-400 bg-red-400/10 border-red-400/30',
    Warm: 'text-orange-400 bg-orange-400/10 border-orange-400/30',
    Cold: 'text-blue-400 bg-blue-400/10 border-blue-400/30'
  }

  const scoreEmoji = { Hot: '🔥', Warm: '⚡', Cold: '❄️' }

  const getBudgetLabel = (budget) => {
    if (budget >= 50000) return { label: 'Enterprise', color: 'text-red-400' }
    if (budget >= 20000) return { label: 'Mid-Range', color: 'text-orange-400' }
    return { label: 'Starter', color: 'text-blue-400' }
  }

  const budgetInfo = getBudgetLabel(form.budget)

  return (
    <div className="max-w-2xl mx-auto p-8">
      <div className="mb-8">
        <h2 className="text-3xl font-bold text-white">🎯 Lead Analysis Form</h2>
        <p className="text-gray-400 mt-2">Fill the form — AI will analyze your lead instantly!</p>
      </div>

      <div className="bg-gray-900 rounded-xl p-6 space-y-4 border border-gray-800">

        <div className="grid grid-cols-2 gap-4">
          <input
            placeholder="Full Name"
            value={form.name}
            onChange={e => setForm({...form, name: e.target.value})}
            className="w-full bg-gray-800 text-white rounded-lg px-4 py-3 outline-none border border-gray-700 focus:border-blue-500 transition"
          />
          <input
            placeholder="Email Address"
            value={form.email}
            onChange={e => setForm({...form, email: e.target.value})}
            className="w-full bg-gray-800 text-white rounded-lg px-4 py-3 outline-none border border-gray-700 focus:border-blue-500 transition"
          />
        </div>

        <input
          placeholder="Company Name"
          value={form.company}
          onChange={e => setForm({...form, company: e.target.value})}
          className="w-full bg-gray-800 text-white rounded-lg px-4 py-3 outline-none border border-gray-700 focus:border-blue-500 transition"
        />

        {/* Budget Slider */}
        <div className="bg-gray-800 rounded-lg p-4 border border-gray-700">
          <div className="flex justify-between items-center mb-3">
            <span className="text-gray-400 text-sm">💰 Budget</span>
            <div className="flex items-center gap-2">
              <span className="text-white font-bold text-lg">
                ${form.budget.toLocaleString()}
              </span>
              <span className={`text-xs font-medium px-2 py-1 rounded-full bg-gray-700 ${budgetInfo.color}`}>
                {budgetInfo.label}
              </span>
            </div>
          </div>
          <input
            type="range"
            min="1000"
            max="100000"
            step="1000"
            value={form.budget}
            onChange={e => setForm({...form, budget: parseInt(e.target.value)})}
            className="w-full accent-blue-500"
          />
          <div className="flex justify-between text-gray-500 text-xs mt-1">
            <span>$1,000</span>
            <span>$50,000</span>
            <span>$100,000</span>
          </div>
        </div>

        <textarea
          placeholder="Requirements — describe what you need..."
          value={form.requirements}
          onChange={e => setForm({...form, requirements: e.target.value})}
          rows={4}
          className="w-full bg-gray-800 text-white rounded-lg px-4 py-3 outline-none border border-gray-700 focus:border-blue-500 transition resize-none"
        />

        <button
          onClick={handleSubmit}
          disabled={loading}
          className="w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-700 text-white font-bold py-3 rounded-lg transition flex items-center justify-center gap-2"
        >
          {loading ? (
            <>
              <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"/>
              Analyzing with AI...
            </>
          ) : '🚀 Analyze Lead'}
        </button>
      </div>

      {result && (
        <div className="mt-6 bg-gray-900 rounded-xl p-6 border border-gray-800 space-y-4">
          <h3 className="text-xl font-bold text-white">📊 Analysis Result</h3>

          <div className={`rounded-lg p-4 border ${scoreColor[result.lead_score]}`}>
            <div className="flex items-center gap-3">
              <span className="text-4xl">{scoreEmoji[result.lead_score]}</span>
              <div>
                <p className="text-sm opacity-70">Lead Score</p>
                <p className="text-2xl font-bold">{result.lead_score} Lead</p>
              </div>
            </div>
          </div>

          {result.ai_email && (
            <div className="bg-gray-800 rounded-lg p-4 border border-gray-700">
              <p className="text-gray-400 text-sm mb-2">📧 AI Generated Email:</p>
              <p className="text-white text-sm whitespace-pre-wrap leading-relaxed">
                {result.ai_email}
              </p>
            </div>
          )}
        </div>
      )}
    </div>
  )
}