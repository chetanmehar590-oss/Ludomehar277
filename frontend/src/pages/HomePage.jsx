import React, { useState, useEffect } from 'react';
import { Card } from '../components/ui/card';
import { Button } from '../components/ui/button';
import { Input } from '../components/ui/input';
import { Checkbox } from '../components/ui/checkbox';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '../components/ui/select';
import { Copy, Pencil } from 'lucide-react';
import { toast } from '../hooks/use-toast';
import {
  tableTypes,
  quickAmounts,
  quickGamePlus,
  tableOptions
} from '../mock';
import {
  getUserBalance,
  getLatestTableRequest,
  createTableRequest
} from '../services/api';

const HomePage = () => {
  const [balance, setBalance] = useState(mockUser.balance);
  const [lastRequest, setLastRequest] = useState(mockLastTableRequest);
  const [amount, setAmount] = useState('');
  const [type, setType] = useState('full');
  const [gamePlus, setGamePlus] = useState('');
  const [selectedOptions, setSelectedOptions] = useState([]);
  const [agreeRules, setAgreeRules] = useState(false);

  const handleCopyTable = () => {
    setAmount(lastRequest.amount.toString());
    setType(lastRequest.type.toLowerCase());
    setGamePlus(lastRequest.gamePlus.toString());
    setSelectedOptions(lastRequest.options);
    toast({
      title: "Table Copied",
      description: "Last table details copied successfully"
    });
  };

  const handleEditTable = () => {
    handleCopyTable();
    window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
  };

  const handleOptionToggle = (optionId) => {
    setSelectedOptions(prev => {
      if (prev.includes(optionId)) {
        return prev.filter(id => id !== optionId);
      } else {
        return [...prev, optionId];
      }
    });
  };

  const handleSendTable = () => {
    if (!amount || parseFloat(amount) <= 0) {
      toast({
        title: "Error",
        description: "Please enter a valid amount",
        variant: "destructive"
      });
      return;
    }

    if (!agreeRules) {
      toast({
        title: "Error",
        description: "Please agree to the game rules",
        variant: "destructive"
      });
      return;
    }

    const newTable = {
      id: `table_${Date.now()}`,
      amount: parseFloat(amount),
      type: type,
      gamePlus: gamePlus ? parseInt(gamePlus) : 0,
      options: selectedOptions,
      timestamp: new Date().toISOString()
    };

    setLastRequest(newTable);
    
    // Reset form
    setAmount('');
    setType('full');
    setGamePlus('');
    setSelectedOptions([]);
    setAgreeRules(false);

    toast({
      title: "Table Sent Successfully!",
      description: `Your table request for ₹${amount} has been submitted`
    });
  };

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white border-b-2 border-gray-200 py-4 px-4">
        <div className="max-w-4xl mx-auto flex items-center gap-3">
          <div className="w-12 h-12 bg-green-700 rounded-full flex items-center justify-center text-white font-bold">
            DN
          </div>
          <h1 className="text-2xl font-bold tracking-wide">DEEP NIGHT LUDO CLUB</h1>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-4xl mx-auto px-4 py-6">
        {/* Table Details Header */}
        <div className="bg-white border-b-2 border-gray-200 px-6 py-4 mb-0">
          <div className="flex justify-between items-center">
            <h2 className="text-2xl font-bold">Table Details</h2>
            <div className="flex items-center gap-2 text-green-600">
              <span className="text-xl font-bold">Balance: ₹{balance.toFixed(2)}</span>
            </div>
          </div>
        </div>

        {/* Last Table Request Card */}
        <Card className="mb-6 p-6 bg-white shadow-sm border-2 border-gray-200">
          <div className="space-y-4">
            <div className="flex items-center gap-2 mb-3">
              <div className="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center text-blue-600 font-bold text-sm">
                1
              </div>
              <h3 className="text-xl font-bold">Last Table Request</h3>
            </div>
            
            <div className="flex items-center gap-4 text-lg">
              <span className="text-2xl">💰</span>
              <span className="font-bold">₹{lastRequest.amount.toFixed(2)}</span>
              <span className="text-2xl">🎲</span>
              <span className="font-semibold">{lastRequest.type}</span>
              <span className="text-2xl">📊</span>
              <span>{lastRequest.gamePlus}</span>
            </div>
            
            <div className="flex items-center gap-2 text-base">
              <span className="text-xl">⚙️</span>
              <span className="font-semibold">Options:</span>
              <span>{lastRequest.options.length > 0 ? lastRequest.options.join(', ') : 'None'}</span>
            </div>

            <div className="flex gap-3 mt-4">
              <Button
                onClick={handleCopyTable}
                variant="outline"
                className="flex-1 text-base py-6 border-2 border-gray-300 hover:bg-gray-100"
              >
                <span className="text-xl mr-2">🔄</span>
                Copy Table
              </Button>
              <Button
                onClick={handleEditTable}
                variant="outline"
                className="flex-1 text-base py-6 border-2 border-gray-300 hover:bg-gray-100"
              >
                <span className="text-xl mr-2">✏️</span>
                Edit Table
              </Button>
            </div>
          </div>
        </Card>

        {/* Amount Section */}
        <div className="bg-white p-6 mb-4 shadow-sm border-2 border-gray-200">
          <div className="flex items-center gap-2 mb-3">
            <span className="text-2xl">💰</span>
            <h3 className="text-xl font-bold">Amount</h3>
          </div>
          <Input
            type="number"
            placeholder="Enter amount"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            className="mb-4 text-lg py-6 border-2"
          />
          <div className="flex flex-wrap gap-2">
            {quickAmounts.map((amt) => (
              <Button
                key={amt}
                onClick={() => setAmount(amt.toString())}
                variant="outline"
                className="text-base px-6 py-5 border-2 border-gray-300 hover:bg-gray-100"
              >
                ₹{amt}
              </Button>
            ))}
          </div>
        </div>

        {/* Type Section */}
        <div className="bg-white p-6 mb-4 shadow-sm border-2 border-gray-200">
          <div className="flex items-center gap-2 mb-3">
            <span className="text-2xl">🎲</span>
            <h3 className="text-xl font-bold">Type</h3>
          </div>
          <Select value={type} onValueChange={setType}>
            <SelectTrigger className="text-lg py-6 border-2">
              <SelectValue />
            </SelectTrigger>
            <SelectContent>
              {tableTypes.map((t) => (
                <SelectItem key={t.value} value={t.value} className="text-lg">
                  {t.label}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        </div>

        {/* Game+ Section */}
        <div className="bg-white p-6 mb-4 shadow-sm border-2 border-gray-200">
          <div className="flex items-center gap-2 mb-3">
            <span className="text-2xl">📊</span>
            <h3 className="text-xl font-bold">Game+</h3>
          </div>
          <Input
            type="number"
            placeholder="Enter Game+"
            value={gamePlus}
            onChange={(e) => setGamePlus(e.target.value)}
            className="mb-4 text-lg py-6 border-2"
          />
          <div className="flex flex-wrap gap-2">
            {quickGamePlus.map((gp) => (
              <Button
                key={gp}
                onClick={() => setGamePlus(gp.toString())}
                variant="outline"
                className="text-base px-6 py-5 border-2 border-gray-300 hover:bg-gray-100"
              >
                {gp}+
              </Button>
            ))}
          </div>
        </div>

        {/* Options Section */}
        <div className="bg-white p-6 mb-4 shadow-sm border-2 border-gray-200">
          <div className="flex items-center gap-2 mb-4">
            <span className="text-2xl">⚙️</span>
            <h3 className="text-xl font-bold">Options</h3>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {tableOptions.map((option) => (
              <div key={option.id} className="flex items-center space-x-3 border-2 border-gray-300 rounded-lg p-4 hover:bg-gray-50">
                <Checkbox
                  id={option.id}
                  checked={selectedOptions.includes(option.id)}
                  onCheckedChange={() => handleOptionToggle(option.id)}
                  className="w-5 h-5"
                />
                <label
                  htmlFor={option.id}
                  className="text-base font-medium cursor-pointer flex-1"
                >
                  {option.label}
                </label>
              </div>
            ))}
          </div>
        </div>

        {/* Agreement */}
        <div className="bg-white p-6 mb-4 shadow-sm border-2 border-gray-200">
          <div className="flex items-start space-x-3">
            <Checkbox
              id="agree-rules"
              checked={agreeRules}
              onCheckedChange={setAgreeRules}
              className="w-5 h-5 mt-1"
            />
            <label htmlFor="agree-rules" className="text-base cursor-pointer">
              I am agree with the{' '}
              <a href="#" className="text-cyan-500 underline hover:text-cyan-600">
                Game Rules
              </a>
            </label>
          </div>
        </div>

        {/* Send Button */}
        <Button
          onClick={handleSendTable}
          className="w-full bg-teal-700 hover:bg-teal-800 text-white text-lg py-7 font-semibold"
          disabled={!agreeRules}
        >
          <span className="text-xl mr-2">✅</span>
          Send Table
        </Button>
      </div>
    </div>
  );
};

export default HomePage;
