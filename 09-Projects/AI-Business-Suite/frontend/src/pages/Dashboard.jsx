import { useState, useEffect } from 'react'
import { PieChart, Pie, Cell, Tooltip, Legend, ResponsiveContainer } from 'recharts'

const COLORS = { Hot: '#ef4444', Warm: '#f97316', Cold: '#3b82f6' }

export default function Dashboard() {
  const [leads, setLeads] = useState([])

  useEffect(() => {
    const saved = JSON.parse(localStorage.getItem('leads') || '[]')
    setLeads(saved)
  }, [])

  const stats = {
    total: leads.length,
    hot: leads.filter(l => l.lead_score === 'Hot').length,
    warm: leads.filter(l => l.lead_score === 'Warm').length,
    cold: leads.filter(l => l.lead_score === 'Cold').length,
  }

  const pieData = [
    { name: 'Hot', value: stats.hot },
    { name: 'Warm', value: stats.warm },
    { name: 'Cold', value: stats.cold },
  ].filter(d => d.value > 0)

  return (
    <div className="max-w-6xl mx-auto p-8">
      <h2 className="text-3xl font-bold text-white mb-8">📊 Dashboard</h2>

      {/* Stats Cards */}
      <div className="grid grid-cols-4 gap-4 mb-8">
        {[
          { label: 'Total Leads', value: stats.total, color: 'text-white' },
          { label: '🔥 Hot Leads', value: stats.hot, color: 'text-red-400' },
          { label: '⚡ Warm Leads', value: stats.warm, color: 'text-orange-400' },
          { label: '❄️ Cold Leads', value: stats.cold, color: 'text-blue-400' },
        ].map(stat => (
          <div key={stat.label} className="bg-gray-900 rounded-xl p-6 border border-gray-800">
            <p className="text-gray-400 text-sm">{stat.label}</p>
            <p className={`text-4xl font-bold mt-2 ${stat.color}`}>{stat.value}</p>
          </div>
        ))}
      </div>

      {/* Chart + Table */}
      <div className="grid grid-cols-2 gap-6 mb-8">
        <div className="bg-gray-900 rounded-xl p-6 border border-gray-800">
          <h3 className="text-white font-bold mb-4">Lead Distribution</h3>
          {pieData.length > 0 ? (
            <ResponsiveContainer width="100%" height={250}>
              <PieChart>
                <Pie data={pieData} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={80}>
                  {pieData.map(entry => (
                    <Cell key={entry.name} fill={COLORS[entry.name]} />
                  ))}
                </Pie>
                <Tooltip />
                <Legend />
              </PieChart>
            </ResponsiveContainer>
          ) : (
            <p className="text-gray-500 text-center mt-16">No leads yet!</p>
          )}
        </div>

        <div className="bg-gray-900 rounded-xl p-6 border border-gray-800">
          <h3 className="text-white font-bold mb-4">Quick Stats</h3>
          <div className="space-y-4">
            {[
              { label: 'Hot Rate', value: stats.total ? Math.round(stats.hot/stats.total*100) : 0, color: 'bg-red-500' },
              { label: 'Warm Rate', value: stats.total ? Math.round(stats.warm/stats.total*100) : 0, color: 'bg-orange-500' },
              { label: 'Cold Rate', value: stats.total ? Math.round(stats.cold/stats.total*100) : 0, color: 'bg-blue-500' },
            ].map(item => (
              <div key={item.label}>
                <div className="flex justify-between text-sm mb-1">
                  <span className="text-gray-400">{item.label}</span>
                  <span className="text-white">{item.value}%</span>
                </div>
                <div className="bg-gray-700 rounded-full h-2">
                  <div className={`${item.color} h-2 rounded-full transition-all`} style={{width: `${item.value}%`}}/>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Leads Table */}
      <div className="bg-gray-900 rounded-xl border border-gray-800 overflow-hidden">
        <div className="p-6 border-b border-gray-800">
          <h3 className="text-white font-bold">Lead History</h3>
        </div>
        {leads.length > 0 ? (
          <table className="w-full">
            <thead className="bg-gray-800">
              <tr>
                {['Name', 'Company', 'Budget', 'Score', 'Email'].map(h => (
                  <th key={h} className="text-left text-gray-400 text-sm px-6 py-3">{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {leads.map((lead, i) => (
                <tr key={i} className="border-t border-gray-800 hover:bg-gray-800/50">
                  <td className="px-6 py-4 text-white">{lead.name}</td>
                  <td className="px-6 py-4 text-gray-400">{lead.company}</td>
                  <td className="px-6 py-4 text-gray-400">${lead.budget?.toLocaleString()}</td>
                  <td className="px-6 py-4">
                    <span className={`px-2 py-1 rounded-full text-xs font-bold ${
                      lead.lead_score === 'Hot' ? 'bg-red-400/20 text-red-400' :
                      lead.lead_score === 'Warm' ? 'bg-orange-400/20 text-orange-400' :
                      'bg-blue-400/20 text-blue-400'
                    }`}>
                      {lead.lead_score === 'Hot' ? '🔥' : lead.lead_score === 'Warm' ? '⚡' : '❄️'} {lead.lead_score}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-gray-400 text-sm">{lead.email}</td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p className="text-gray-500 text-center py-16">No leads submitted yet!</p>
        )}
      </div>
    </div>
  )
}