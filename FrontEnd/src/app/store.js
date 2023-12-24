import { configureStore } from '@reduxjs/toolkit';
import mainReducer from '../features/home/mainSlice';

export const store = configureStore({
  reducer: {
    main: mainReducer,
  },
});
