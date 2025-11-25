// Mock data for Deep Night Ludo Club Bot

export const mockUser = {
  id: "user_001",
  balance: 28.00,
  name: "User"
};

export const mockLastTableRequest = {
  id: "table_001",
  amount: 600.00,
  type: "Full",
  gamePlus: 0,
  options: [],
  timestamp: new Date().toISOString()
};

export const mockTableHistory = [
  {
    id: "table_001",
    amount: 600.00,
    type: "Full",
    gamePlus: 0,
    options: [],
    status: "completed",
    timestamp: new Date(Date.now() - 3600000).toISOString()
  },
  {
    id: "table_002",
    amount: 1000.00,
    type: "Half",
    gamePlus: 200,
    options: ["Fresh Id", "No iPhone"],
    status: "pending",
    timestamp: new Date(Date.now() - 7200000).toISOString()
  }
];

export const tableTypes = [
  { value: "full", label: "Full" },
  { value: "ulta", label: "Ulta" },
  { value: "popular", label: "Popular" },
  { value: "3_goti", label: "3 Goti" },
  { value: "2_goti", label: "2 Goti" },
  { value: "1_goti", label: "1 Goti" },
  { value: "1_goti_quick", label: "1 Goti Quick" },
  { value: "snake", label: "Snake" },
  { value: "ulta_snake", label: "Ulta Snake" },
  { value: "snake_re_roll", label: "Snake Re-Roll" },
  { value: "not_cut", label: "Not Cut" }
];

export const quickAmounts = [1000, 2000, 3000, 5000, 7000, 8000, 10000];

export const quickGamePlus = [100, 200, 500, 1000];

export const tableOptions = [
  { id: "fresh_id", label: "Fresh Id" },
  { id: "code_aap_doge", label: "Code aap doge" },
  { id: "no_iphone", label: "No iPhone" },
  { id: "no_king_pass", label: "No king pass" },
  { id: "auto_loss", label: "Auto loss" }
];
