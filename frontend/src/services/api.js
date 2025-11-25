import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API_BASE = `${BACKEND_URL}/api`;

// Default user ID (can be replaced with actual user authentication)
const DEFAULT_USER_ID = 'user_default';

// Table Request APIs
export const createTableRequest = async (tableData) => {
  try {
    const response = await axios.post(`${API_BASE}/tables`, {
      ...tableData,
      user_id: DEFAULT_USER_ID
    });
    return response.data;
  } catch (error) {
    console.error('Error creating table request:', error);
    throw error;
  }
};

export const getTableRequests = async (userId = DEFAULT_USER_ID) => {
  try {
    const response = await axios.get(`${API_BASE}/tables`, {
      params: { user_id: userId }
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching table requests:', error);
    throw error;
  }
};

export const getLatestTableRequest = async (userId = DEFAULT_USER_ID) => {
  try {
    const response = await axios.get(`${API_BASE}/tables/latest/${userId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching latest table request:', error);
    return null;
  }
};

export const updateTableRequest = async (tableId, updateData) => {
  try {
    const response = await axios.put(`${API_BASE}/tables/${tableId}`, updateData);
    return response.data;
  } catch (error) {
    console.error('Error updating table request:', error);
    throw error;
  }
};

export const deleteTableRequest = async (tableId) => {
  try {
    const response = await axios.delete(`${API_BASE}/tables/${tableId}`);
    return response.data;
  } catch (error) {
    console.error('Error deleting table request:', error);
    throw error;
  }
};

// User Balance APIs
export const getUserBalance = async (userId = DEFAULT_USER_ID) => {
  try {
    const response = await axios.get(`${API_BASE}/user/balance/${userId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching user balance:', error);
    return { user_id: userId, balance: 28.00 };
  }
};

export const updateUserBalance = async (userId = DEFAULT_USER_ID, balance) => {
  try {
    const response = await axios.post(`${API_BASE}/user/balance/${userId}`, null, {
      params: { balance }
    });
    return response.data;
  } catch (error) {
    console.error('Error updating user balance:', error);
    throw error;
  }
};
