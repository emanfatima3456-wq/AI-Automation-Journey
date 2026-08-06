import { Link, useLocation } from 'react-router-dom'

export default function Navbar() {
  const location = useLocation()

  return (
    <nav className="bg-gray-900 border-b border-gray-700 px-6 py-4">
      <div className="max-w-7xl mx-auto flex justify-between items-center">
        <h1 className="text-xl font-bold text-white">
          🤖 AI Business Suite
        </h1>
        <div className="flex gap-6">
          <Link
            to="/"
            className={`text-sm font-medium ${
              location.pathname === '/'
                ? 'text-blue-400'
                : 'text-gray-400 hover:text-white'
            }`}
          >
            Lead Form
          </Link>
          <Link
            to="/dashboard"
            className={`text-sm font-medium ${
              location.pathname === '/dashboard'
                ? 'text-blue-400'
                : 'text-gray-400 hover:text-white'
            }`}
          >
            Dashboard
          </Link>
        </div>
      </div>
    </nav>
  )
}